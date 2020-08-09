#!/usr/bin/env python3

##
## @package mapdump
##
## The mapdump command-line tool, by
##
##                     _            __
##    _________  _____(_)__  ____  / /____
##   / ___/ __ \/ ___/ / _ \/ __ \/ __/ _ \
##  (__  ) /_/ / /  / /  __/ / / / /_/  __/
## /____/\____/_/__/ /\___/_/ /_/\__/\___/
##              /___/


import sys
import os
import click

from .definitions import VERSION
from .parser import get_raw_symbols, construct_symbol_list, get_memory_config

@click.command()
@click.argument('mapfile', nargs = 1)
@click.version_option(version = VERSION,
                      prog_name = "mapdump")

def main(mapfile):
    '''Analyzes a .map file in order to examine memory usage.'''
    # check file extension
    if mapfile.endswith('.map'):
        memory_config = get_memory_config(mapfile)
        symbol_list = construct_symbol_list(mapfile)

    else:
        print("The file's extension is not correct. Please provide a .map file.")
        exit(1)


    symbols_per_memory_sector = []

    for i in range(len(memory_config)):
        symbols_per_memory_sector.append([])

    for symbol in symbol_list:
        for i, memory in enumerate(memory_config):
            if symbol.is_in_memory(memory):
                symbols_per_memory_sector[i].append(symbol)
                break


    for i in range(len(symbols_per_memory_sector)):
        sector_size = sum(list(map(lambda x: x.size, symbols_per_memory_sector[i])))
        print(f'{memory_config[i].name}: {sector_size} bytes ({sector_size / memory_config[i].size * 100:.2f}%)')



if __name__ == "__main__":
    '''Program's entry point'''
    main()
