#!/usr/bin/env python3

import re

from .definitions import MEMORY_CONFIG_REGEX, LOCAL_SYMBOL_REGEX, LIB_SYMBOL_REGEX


def get_memory_config(mapfile):
    '''
    Gets the configuration of the memory sections.

    Inputs:
        mapfile: the path to the .map file.
    Outputs:
        A dictionary containing the memory configuration. The dictionary follows the following format:

        memory_config_dict {
            'RAM': [<start address>, <size>],
            'FLASH': [<start address>, <size>],
            ...
            '*default*': [<start address>, <size>]
        }
    '''
    
    with open(mapfile, 'r') as file:
        raw_data = file.read()

    start_pattern = re.compile("Memory Configuration")
    start_index = start_pattern.search(raw_data).start()

    end_pattern = re.compile("Linker script and memory map")
    end_index = end_pattern.search(raw_data).start()

    memory_config_pattern = re.compile(MEMORY_CONFIG_REGEX)
    memory_config_data = memory_config_pattern.findall(raw_data, pos=start_index, endpos=end_index)


    memory_config_dict = {}

    for section in memory_config_data:
        section_name = section[0]
        section_addr = int(section[1], 0)
        section_size = int(section[2], 0)
        
        memory_config_dict[section_name] = [section_addr, section_size]

    return memory_config_dict


def get_raw_symbols(mapfile):
    '''
    Gets raw symbols from a mapfile using the regex defined in defitions.py.

    Inputs:
        mapfile: the path to the .map file.

    Outputs:
        A tuple of two lists of tuples:
            1. Local symbols: each tuple describes a section/symbol that contains one or more subsymbols. The tuple's
               elements are as follows:
                   0. The section/symbol's name
                   1. The symbol's address
                   2. The symbol's size
                   3. The object file containing the symbol
                   4-6. First character of the object file's path, to be ignored
            2. Linked symbols (from external libraries): each tuple describes a section that contains a symbol. The
               tuple's elements are as follows:
                   0. The section's name
                   1. The symbol's address
                   2. The symbol's size
                   3. The object file containing the symbol
                   4-6. First character of the object file's path, to be ignored
                   7. The symbol's name
    '''
    with open(mapfile, 'r') as file:
        raw_data = file.read()

    start_pattern = re.compile("Linker script and memory map")
    start_index = start_pattern.search(raw_data).start()

    local_symbol_pattern = re.compile(LOCAL_SYMBOL_REGEX)
    local_symbols = local_symbol_pattern.findall(raw_data, pos=start_index)

    lib_symbol_pattern = re.compile(LIB_SYMBOL_REGEX)
    lib_symbols = lib_symbol_pattern.findall(raw_data, pos=start_index)

    return local_symbols, lib_symbols


def construct_memory_dict(raw_symbols):
    '''
    Constructs a complete memory dictionary, mapping sizes to symbols.

    Inputs:
        raw_symbols: a pair of lists of tuples, as returned by get_raw_symbols().
    Outputs:
        A memory map dictionary. The dictionary is laid out as follows:

        memory_dict = {
            'local': {
                'local_file.o': {
                    'symbol_1': [<size>, <start address>],
                    'symbol_2': [<size>, <start address>],
                    ...
                },
                ...
            },
            'external': {
                'external_lib_1.a' : {
                    'external_file_1.o' : {
                        'symbol_1': [<size>, <start address>],
                        'symbol_2': [<size>, <start address>],
                        ...
                    },
                    ...
                },
                ...
            }
        }
    '''
    memory_dict = {
        'local': {},
        'external': {}
    }

    local_symbols, lib_symbols = raw_symbols

    for symbol in local_symbols:
        symbol_name = symbol[0].split('.')[-1]
        symbol_addr = int(symbol[1], 0)
        symbol_size = int(symbol[2], 0)
        symbol_file = symbol[3]

        if symbol_file not in memory_dict['local']:
            memory_dict['local'][symbol_file] = { symbol_name: [symbol_size, symbol_addr] }
        else:
            memory_dict['local'][symbol_file][symbol_name] = [symbol_size, symbol_addr]


    for symbol in lib_symbols:
        symbol_name = symbol[7]
        symbol_addr = int(symbol[1], 0)
        symbol_size = int(symbol[2], 0)
        lib_file = symbol[3].split('(')[0]
        obj_file = symbol[3].split('(')[1].split(')')[0]

        if lib_file not in memory_dict['external']:
            memory_dict['external'][lib_file] = {
                obj_file: {
                    symbol_name: [symbol_size, symbol_addr]
                }
            }
        else:
            if obj_file not in memory_dict['external'][lib_file]:
                memory_dict['external'][lib_file][obj_file] = { symbol_name: [symbol_size, symbol_addr] }
            else:
                memory_dict['external'][lib_file][obj_file][symbol_name] = [symbol_size, symbol_addr]

    return memory_dict['local']
