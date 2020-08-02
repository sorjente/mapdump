#!/usr/bin/env python3

import unittest
import os

from mapdump.parser import get_memory_config
from mapdump.memory import Memory


DUMMY_DATA_DIR    = "./mapdump/tests/dummy_data/"
SIMPLE_BLINKY_MAP = os.path.join(DUMMY_DATA_DIR, "simple_blinky.map")
CUSTOM_PCB_MAP    = os.path.join(DUMMY_DATA_DIR, "custom_pcb.map")


class TestParser(unittest.TestCase):
    
    def test_memory_configuration_parsing(self):
        # Get memory configuration
        simple_blinky_memconf = get_memory_config(SIMPLE_BLINKY_MAP)
        custom_pcb_memconf = get_memory_config(CUSTOM_PCB_MAP)

        # Each .map file should have 3 sectors: RAM, FLASH and *default*
        self.assertEqual(len(simple_blinky_memconf), 3)
        self.assertEqual(len(custom_pcb_memconf), 3)

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
