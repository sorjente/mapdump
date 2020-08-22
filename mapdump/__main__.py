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
from .parser import get_raw_symbols, construct_symbol_list, get_memory_config, construct_file_size_dict

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


    for memory in memory_config:
        # Skip *default* section
        if memory.name == '*default*':
            continue
        
        # Get the symbols that are in this memory sector
        symbols_in_memory = list(filter(lambda s: s.is_in_memory(memory), symbol_list))
        
        # If there are no symbols, skip the sector
        if len(symbols_in_memory) == 0:
            continue

        # Print the sector's name and a separator line of *
        print(memory)
        print('*' * 40)

        # Get the total memory used in this sector (in bytes)
        memory_size_used = sum(list(map(lambda s: s.size, symbols_in_memory)))

        # Get and sort the files based on the place they take on this sector
        file_size_dict = construct_file_size_dict(symbols_in_memory)
        sorted_file_list = [(k, v) for k, v in sorted(file_size_dict.items(), key=lambda item: item[1], reverse=True)]

        # Get the length of the longest filename (for pretty printing)
        max_file_name_length = max(list(map(lambda x: len(x[0]), sorted_file_list)))

        # Print the files in descending order
        for file, size in sorted_file_list:
            print(f'\t{file} {" " * (max_file_name_length - len(file))} '\
                  f'[{size} bytes, {size / memory_size_used * 100:.2f}% of {memory.name} space used]')

        # Print a space except if it's the last memory sector
        if memory != memory_config[-1]:
            print()



if __name__ == "__main__":
    '''Program's entry point'''
    main()
