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
from .parser import get_raw_symbols, construct_memory_dict, get_memory_config

@click.command()
@click.argument('mapfile', nargs = 1)
@click.version_option(version = VERSION,
                      prog_name = "mapdump")

def main(mapfile):
    '''Analyzes a .map file in order to examine memory usage.'''
    # check file extension
    if mapfile.endswith('.map'):
        print(get_memory_config(mapfile))
        print(construct_memory_dict(get_raw_symbols(mapfile)))
    else:
        print("The file's extension is not correct. Please provide a .map file.")
        exit(1)

if __name__ == "__main__":
    '''Program's entry point'''
    main()
