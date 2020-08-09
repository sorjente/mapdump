#!/usr/bin/env python3

import unittest
import os

from mapdump.parser import get_memory_config, get_raw_symbols, construct_symbol_list
from mapdump.memory import Memory
from mapdump.symbol import Symbol

from mapdump.tests.test_data import simple_blinky_raw_local_symbols, simple_blinky_raw_lib_symbols,\
                                    simple_blinky_raw_common_symbols, simple_blinky_raw_fill_symbols,\
                                    simple_blinky_parsed_symbols



DUMMY_DATA_DIR    = "./mapdump/tests/dummy_data/"
SIMPLE_BLINKY_MAP = os.path.join(DUMMY_DATA_DIR, "simple_blinky.map")
CUSTOM_PCB_MAP    = os.path.join(DUMMY_DATA_DIR, "custom_pcb.map")


class TestParser(unittest.TestCase):
    
    def test_memory_configuration_parsing(self):
        # Get memory configuration
        simple_blinky_memconf = get_memory_config(SIMPLE_BLINKY_MAP)
        custom_pcb_memconf = get_memory_config(CUSTOM_PCB_MAP)

        # Each .map file should have 2 sectors: RAM and FLASH (*default* is discarded)
        self.assertEqual(len(simple_blinky_memconf), 2)
        self.assertEqual(len(custom_pcb_memconf), 2)

        # Check that the sectors are Memory objects
        self.assertIsInstance(simple_blinky_memconf[0], Memory)
        self.assertIsInstance(simple_blinky_memconf[1], Memory)
        self.assertIsInstance(custom_pcb_memconf[0], Memory)
        self.assertIsInstance(custom_pcb_memconf[1], Memory)

        # Check sector names, addresses and sizes
        self.assertEqual(simple_blinky_memconf[0].name, "RAM")
        self.assertEqual(simple_blinky_memconf[0].address, 0x20000000)
        self.assertEqual(simple_blinky_memconf[0].size, 0x5000)
        self.assertEqual(simple_blinky_memconf[1].name, "FLASH")
        self.assertEqual(simple_blinky_memconf[1].address, 0x8000000)
        self.assertEqual(simple_blinky_memconf[1].size, 0x20000)

        self.assertEqual(custom_pcb_memconf[0].name, "RAM")
        self.assertEqual(custom_pcb_memconf[0].address, 0x20000000)
        self.assertEqual(custom_pcb_memconf[0].size, 0x28000)
        self.assertEqual(custom_pcb_memconf[1].name, "FLASH")
        self.assertEqual(custom_pcb_memconf[1].address, 0x8000000)
        self.assertEqual(custom_pcb_memconf[1].size, 0x80000)


    def test_raw_symbol_parsing(self):
        # Get raw symbols
        local, lib, common, fill = get_raw_symbols(SIMPLE_BLINKY_MAP)

        # Ensure that all symbols are parsed
        self.assertEqual(len(local), len(simple_blinky_raw_local_symbols),
                         f'Failed to parse all local symbols ({len(local)}/{len(simple_blinky_raw_local_symbols)}).')
        self.assertEqual(len(lib), len(simple_blinky_raw_lib_symbols),
                         f'Failed to parse all external (lib) symbols '\
                         f'({len(lib)}/{len(simple_blinky_raw_lib_symbols)}).')
        self.assertEqual(len(common), len(simple_blinky_raw_common_symbols), 
                         f'Failed to parse all COMMON symbols ({len(common)}/{len(simple_blinky_raw_common_symbols)}).')
        self.assertEqual(len(fill), len(simple_blinky_raw_fill_symbols),
                         f'Failed to parse all *fill* symbols ({len(fill)}/{len(simple_blinky_raw_fill_symbols)}).')

        local_items = len(simple_blinky_raw_local_symbols[0])
        lib_items = len(simple_blinky_raw_lib_symbols[0])
        common_items = len(simple_blinky_raw_common_symbols[0])
        fill_items = len(simple_blinky_raw_fill_symbols[0])

        # Check that the symbols are correct
        for i in range(len(simple_blinky_raw_local_symbols)):
            for j in range(local_items):
                self.assertEqual(local[i][j], simple_blinky_raw_local_symbols[i][j],
                                 f'Wrong local symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(simple_blinky_raw_lib_symbols)):
            for j in range(lib_items):
                self.assertEqual(lib[i][j], simple_blinky_raw_lib_symbols[i][j],
                                 f'Wrong external (lib) symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(simple_blinky_raw_common_symbols)):
            for j in range(common_items):
                self.assertEqual(common[i][j], simple_blinky_raw_common_symbols[i][j],
                                 f'Wrong COMMON symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(simple_blinky_raw_fill_symbols)):
            for j in range(fill_items):
                self.assertEqual(fill[i][j], simple_blinky_raw_fill_symbols[i][j],
                                 f'Wrong *fill* symbol (symbol number {i}, tuple element {j}.')


    def test_symbol_list_construction(self):
        symbol_list = construct_symbol_list(SIMPLE_BLINKY_MAP)

        # Ensure that all symbols are parsed
        self.assertEqual(len(symbol_list), len(simple_blinky_parsed_symbols),
                         f'Failed to parse all symbols ({len(symbol_list)}/{len(simple_blinky_parsed_symbols)}).')

        # Verify that each attribute is correct
        for i in range(len(symbol_list)):
            self.assertEqual(symbol_list[i].name, simple_blinky_parsed_symbols[i].name,
                             f'Name not equal for symbol #{i}.')
            self.assertEqual(symbol_list[i].address, simple_blinky_parsed_symbols[i].address,
                             f'Address not equal for symbol #{i}.')
            self.assertEqual(symbol_list[i].size, simple_blinky_parsed_symbols[i].size,
                             f'Size not equal for symbol #{i}.')
            self.assertEqual(symbol_list[i].section, simple_blinky_parsed_symbols[i].section,
                             f'Section not equal for symbol #{i}.')
            self.assertEqual(symbol_list[i].file, simple_blinky_parsed_symbols[i].file,
                             f'File not equal for symbol #{i}.')
            self.assertEqual(symbol_list[i].lib, simple_blinky_parsed_symbols[i].lib,
                             f'Lib not equal for symbol #{i}.')
