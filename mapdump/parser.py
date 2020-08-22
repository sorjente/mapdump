#!/usr/bin/env python3

import re

from .definitions import MEMORY_CONFIG_REGEX, LOCAL_SYMBOL_REGEX, LIB_SYMBOL_REGEX, COMMON_SYMBOL_REGEX,\
                         FILL_SYMBOL_REGEX
from .symbol import Symbol
from .memory import Memory


def get_memory_config(mapfile):
    '''
    Gets the configuration of the memory sections.

    Inputs:
        mapfile: the path to the .map file.
    Outputs:
        A list containing the memory configurations (aka the different memory sectors).
    '''
    
    with open(mapfile, 'r') as file:
        raw_data = file.read()

    start_pattern = re.compile("Memory Configuration")
    start_index = start_pattern.search(raw_data).start()

    end_pattern = re.compile("Linker script and memory map")
    end_index = end_pattern.search(raw_data).start()

    memory_config_pattern = re.compile(MEMORY_CONFIG_REGEX)
    memory_config_data = memory_config_pattern.findall(raw_data, pos=start_index, endpos=end_index)


    memory_config_list = []

    for sector in memory_config_data:
        sector_name = sector[0]
        sector_addr = int(sector[1], 0)
        sector_size = int(sector[2], 0)
        
        # Skip the default sector
        if sector_name != "*default*":
            memory_config_list.append(Memory(name=sector_name,
                                             address=sector_addr,
                                             size=sector_size))

    return memory_config_list


def get_raw_symbols(mapfile):
    '''
    Gets raw symbols from a mapfile using the regex defined in defitions.py.

    Inputs:
        mapfile: the path to the .map file.

    Outputs:
        A tuple of 4 lists of tuples:
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
            3. Common symbols (symbols in COMMON section): each tuple describes a section/symbol that contains one or
               more subsymbols. The tuple's elements are as follows:
                   0. The symbol's address
                   1. The symbol's size
                   2. The object file containing the symbol
                   3-5. First character of the object file's path, to be ignored
                   6. The symbol's name
            4. Fill/padding space: each tuple contains some padding/filler space. The tuple's elements are as follows:
                   0. The address of the padding
                   1. The size of the padding
    '''
    with open(mapfile, 'r') as file:
        raw_data = file.read()

    start_pattern = re.compile("Linker script and memory map")
    start_index = start_pattern.search(raw_data).start()

    # This end pattern is not present in all .map files; however, it doesn't matter because if it is not there we will
    # search until the end of the file
    end_pattern = re.compile("/DISCARD/")
    end_index = end_pattern.search(raw_data)
    # If no index is found, take the maximum index, else take the start of the index found
    if end_index == None:
        end_index = len(raw_data) - 1
    else:
        end_index = end_index.start()

    local_symbol_pattern = re.compile(LOCAL_SYMBOL_REGEX)
    local_symbols = local_symbol_pattern.findall(raw_data, pos=start_index, endpos=end_index)

    lib_symbol_pattern = re.compile(LIB_SYMBOL_REGEX)
    lib_symbols = lib_symbol_pattern.findall(raw_data, pos=start_index, endpos=end_index)

    common_symbol_pattern = re.compile(COMMON_SYMBOL_REGEX)
    common_symbols = common_symbol_pattern.findall(raw_data, pos=start_index, endpos=end_index)

    fill_symbol_pattern = re.compile(FILL_SYMBOL_REGEX)
    fill_symbols = fill_symbol_pattern.findall(raw_data, pos=start_index, endpos=end_index)

    return local_symbols, lib_symbols, common_symbols, fill_symbols


def construct_symbol_list(mapfile):
    '''
    Constructs a complete memory dictionary, mapping sizes to symbols.

    Inputs:
        mapfile: the path to the .map file.
    Outputs:
        A symbol list, containing Symbol objects.
    '''

    symbol_list = []
    local_symbols, lib_symbols, common_symbols, fill_symbols = get_raw_symbols(mapfile)

    for symbol in local_symbols:
        if len(symbol[0].split('.')) > 1:
            symbol_name = '.'.join(symbol[0].split('.')[1:])
        else:
            symbol_name = symbol[0].split('.')[0]

        symbol_section = symbol[0].split('.')[0]
        symbol_addr = int(symbol[1], 0)
        symbol_size = int(symbol[2], 0)
        symbol_file = symbol[3]

        if symbol_size > 0:
            symbol_list.append(Symbol(name=symbol_name,
                                      section=symbol_section,
                                      address=symbol_addr,
                                      size=symbol_size,
                                      file=symbol_file))

    for symbol in lib_symbols:
        symbol_name = symbol[7]
        symbol_section = symbol[0].split('.')[0]
        symbol_addr = int(symbol[1], 0)
        symbol_size = int(symbol[2], 0)
        lib_file = symbol[3].split('(')[0]
        obj_file = symbol[3].split('(')[1].split(')')[0]

        if symbol_size > 0:
            symbol_list.append(Symbol(name=symbol_name,
                                      section=symbol_section,
                                      address=symbol_addr,
                                      size=symbol_size,
                                      file=obj_file,
                                      lib=lib_file))


    for symbol in common_symbols:
        symbol_name = symbol[6]
        symbol_section = "COMMON"
        symbol_addr = int(symbol[0], 0)
        symbol_size = int(symbol[1], 0)
        symbol_file = symbol[2]

        if symbol_size > 0:
            symbol_list.append(Symbol(name=symbol_name,
                                      section=symbol_section,
                                      address=symbol_addr,
                                      size=symbol_size,
                                      file=symbol_file))

    for symbol in fill_symbols:
        symbol_name = "*fill*"
        symbol_section = "*fill*"
        symbol_addr = int(symbol[0], 0)
        symbol_size = int(symbol[1], 0)
        symbol_file = None

        if symbol_size > 0:
            symbol_list.append(Symbol(name=symbol_name,
                                      section=symbol_section,
                                      address=symbol_addr,
                                      size=symbol_size,
                                      file=symbol_file))

    return symbol_list


def construct_file_size_dict(symbol_list):
    '''
    Constructs a dictionary with object (.o) files as the keys, and the size they occupy as their values.

    Input:
        A list of Symbols.
    Output:
        A dictionary in {file:size} form.
    '''
    file_size_dict = {}

    for symbol in symbol_list:
        key = symbol.file

        if symbol.is_external():
            # Add the library if the symbol is external
            key += f' ({symbol.lib})'
        elif symbol.file == None:
            # No file means that the symbol is padding/filler
            key = '*fill*'

        if key not in file_size_dict:
            file_size_dict[key] = symbol.size
        else:
            file_size_dict[key] += symbol.size

    return file_size_dict
