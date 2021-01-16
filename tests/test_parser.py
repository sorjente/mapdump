import pytest
import os


from mapdump.parser import get_memory_config, get_raw_symbols, construct_symbol_list
from mapdump.memory import Memory
from mapdump.symbol import Symbol

from tests.test_data import (
    simple_blinky_raw_local_symbols,
    simple_blinky_raw_lib_symbols,
    simple_blinky_raw_common_symbols,
    simple_blinky_raw_fill_symbols,
    simple_blinky_parsed_symbols,
)


DUMMY_DATA_DIR = "./tests/dummy_data/"
SIMPLE_BLINKY_MAP = os.path.join(DUMMY_DATA_DIR, "simple_blinky.map")
CUSTOM_PCB_MAP = os.path.join(DUMMY_DATA_DIR, "custom_pcb.map")


class TestParser:
    def test_memory_configuration_parsing(self):
        # Get memory configuration
        simple_blinky_memconf = get_memory_config(SIMPLE_BLINKY_MAP)
        custom_pcb_memconf = get_memory_config(CUSTOM_PCB_MAP)

        # Each .map file should have 2 sectors: RAM and FLASH (*default* is discarded)
        assert len(simple_blinky_memconf) == 2
        assert len(custom_pcb_memconf) == 2

        # Check that the sectors are Memory objects
        assert type(simple_blinky_memconf[0]) == Memory
        assert type(simple_blinky_memconf[1]) == Memory
        assert type(custom_pcb_memconf[0]) == Memory
        assert type(custom_pcb_memconf[1]) == Memory

        # Check sector names, addresses and sizes
        assert simple_blinky_memconf[0].name == "RAM"
        assert simple_blinky_memconf[0].address == 0x20000000
        assert simple_blinky_memconf[0].size == 0x5000
        assert simple_blinky_memconf[1].name == "FLASH"
        assert simple_blinky_memconf[1].address == 0x8000000
        assert simple_blinky_memconf[1].size == 0x20000

        assert custom_pcb_memconf[0].name == "RAM"
        assert custom_pcb_memconf[0].address == 0x20000000
        assert custom_pcb_memconf[0].size == 0x28000
        assert custom_pcb_memconf[1].name == "FLASH"
        assert custom_pcb_memconf[1].address == 0x8000000
        assert custom_pcb_memconf[1].size == 0x80000

    def test_raw_symbol_parsing(self):
        # Get raw symbols
        local, lib, common, fill = get_raw_symbols(SIMPLE_BLINKY_MAP)

        # Ensure that all symbols are parsed
        assert len(local) == len(simple_blinky_raw_local_symbols)
        assert len(lib) == len(simple_blinky_raw_lib_symbols)
        assert len(common) == len(simple_blinky_raw_common_symbols)
        assert len(fill) == len(simple_blinky_raw_fill_symbols)

        local_items = len(simple_blinky_raw_local_symbols[0])
        lib_items = len(simple_blinky_raw_lib_symbols[0])
        common_items = len(simple_blinky_raw_common_symbols[0])
        fill_items = len(simple_blinky_raw_fill_symbols[0])

        # Check that the symbols are correct
        for i in range(len(simple_blinky_raw_local_symbols)):
            for j in range(local_items):
                assert (
                    local[i][j] == simple_blinky_raw_local_symbols[i][j]
                ), f"Wrong local symbol (symbol number {i}, tuple element {j}."

        for i in range(len(simple_blinky_raw_lib_symbols)):
            for j in range(lib_items):
                assert (
                    lib[i][j] == simple_blinky_raw_lib_symbols[i][j]
                ), f"Wrong external (lib) symbol (symbol number {i}, tuple element {j}."

        for i in range(len(simple_blinky_raw_common_symbols)):
            for j in range(common_items):
                assert (
                    common[i][j] == simple_blinky_raw_common_symbols[i][j]
                ), f"Wrong COMMON symbol (symbol number {i}, tuple element {j}."

        for i in range(len(simple_blinky_raw_fill_symbols)):
            for j in range(fill_items):
                assert (
                    fill[i][j] == simple_blinky_raw_fill_symbols[i][j]
                ), f"Wrong *fill* symbol (symbol number {i}, tuple element {j}."

    def test_symbol_list_construction(self):
        symbol_list = construct_symbol_list(SIMPLE_BLINKY_MAP)

        # Ensure that all symbols are parsed
        assert len(symbol_list) == len(simple_blinky_parsed_symbols)

        # Verify that each attribute is correct
        for i in range(len(symbol_list)):
            assert (
                symbol_list[i].name == simple_blinky_parsed_symbols[i].name
            ), f"Name not equal for symbol #{i}."

            assert (
                symbol_list[i].address == simple_blinky_parsed_symbols[i].address
            ), f"Address not equal for symbol #{i}."

            assert (
                symbol_list[i].size == simple_blinky_parsed_symbols[i].size
            ), f"Size not equal for symbol #{i}."

            assert (
                symbol_list[i].section == simple_blinky_parsed_symbols[i].section
            ), f"Section not equal for symbol #{i}."

            assert (
                symbol_list[i].file == simple_blinky_parsed_symbols[i].file
            ), f"File not equal for symbol #{i}."

            assert (
                symbol_list[i].lib == simple_blinky_parsed_symbols[i].lib
            ), f"Lib not equal for symbol #{i}."
