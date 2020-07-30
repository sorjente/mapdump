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
        #print(get_memory_config(mapfile))
        #print(construct_symbol_list(get_raw_symbols(mapfile))[20])
        

        memory_config = get_memory_config(mapfile)
        symbol_list = construct_symbol_list(mapfile)
    else:
        print("The file's extension is not correct. Please provide a .map file.")
        exit(1)


    for memory in memory_config:
        if memory.name == '*default*':
            continue
        print(memory)
        for symbol in symbol_list:
            if symbol.is_in_memory(memory):
                print('\t', end='')
                print(symbol)



if __name__ == "__main__":
    '''Program's entry point'''
    main()
