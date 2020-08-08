#!/usr/bin/env python3

import unittest
import os

from mapdump.parser import get_memory_config, get_raw_symbols, construct_symbol_list
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


    def test_raw_symbol_parsing(self):
        # Get raw symbols
        local, lib, common, fill = get_raw_symbols(SIMPLE_BLINKY_MAP)

        local_symbols = [
            ('isr_vector', '0x0000000008000000', '0x10c', 'build/startup_stm32f103xb.o', 'b', '', ''),
            ('text', '0x000000000800010c', '0x40', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('text.MX_GPIO_Init', '0x000000000800014c', '0x50', 'build/main.o', 'b', '', ''),
            ('text.SystemClock_Config', '0x000000000800019c', '0x50', 'build/main.o', 'b', '', ''),
            ('text.main', '0x00000000080001ec', '0x24', 'build/main.o', 'b', '', ''),
            ('text.NMI_Handler', '0x0000000008000210', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.HardFault_Handler', '0x0000000008000212', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.MemManage_Handler', '0x0000000008000214', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.BusFault_Handler', '0x0000000008000216', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.UsageFault_Handler', '0x0000000008000218', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.SVC_Handler', '0x000000000800021a', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.DebugMon_Handler', '0x000000000800021c', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.PendSV_Handler', '0x000000000800021e', '0x2', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.SysTick_Handler', '0x0000000008000220', '0x8', 'build/stm32f1xx_it.o', 'b', '', ''),
            ('text.HAL_MspInit', '0x0000000008000228', '0x44', 'build/stm32f1xx_hal_msp.o', 'b', '', ''),
            ('text.HAL_InitTick', '0x000000000800026c', '0x4c', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('text.HAL_Init', '0x00000000080002b8', '0x24', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('text.HAL_IncTick', '0x00000000080002dc', '0x18', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('text.HAL_GetTick', '0x00000000080002f4', '0xc', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('text.HAL_Delay', '0x0000000008000300', '0x28', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('text.RCC_Delay', '0x0000000008000328', '0x2c', 'build/stm32f1xx_hal_rcc.o', 'b', '', ''),
            ('text.HAL_RCC_OscConfig', '0x0000000008000354', '0x410', 'build/stm32f1xx_hal_rcc.o', 'b', '', ''),
            ('text.HAL_RCC_GetSysClockFreq', '0x0000000008000764', '0x6c', 'build/stm32f1xx_hal_rcc.o', 'b', '', ''),
            ('text.HAL_RCC_ClockConfig', '0x00000000080007d0', '0x16c', 'build/stm32f1xx_hal_rcc.o', 'b', '', ''),
            ('text.HAL_GPIO_Init', '0x000000000800093c', '0x220', 'build/stm32f1xx_hal_gpio.o', 'b', '', ''),
            ('text.HAL_GPIO_WritePin', '0x0000000008000b5c', '0xc', 'build/stm32f1xx_hal_gpio.o', 'b', '', ''),
            ('text.HAL_GPIO_TogglePin', '0x0000000008000b68', '0xe', 'build/stm32f1xx_hal_gpio.o', 'b', '', ''),
            ('text.HAL_NVIC_SetPriorityGrouping', '0x0000000008000b78', '0x24', 'build/stm32f1xx_hal_cortex.o', 'b', '', ''),
            ('text.HAL_NVIC_SetPriority', '0x0000000008000b9c', '0x68', 'build/stm32f1xx_hal_cortex.o', 'b', '', ''),
            ('text.HAL_SYSTICK_Config', '0x0000000008000c04', '0x2c', 'build/stm32f1xx_hal_cortex.o', 'b', '', ''),
            ('text.SystemInit', '0x0000000008000c30', '0x4c', 'build/system_stm32f1xx.o', 'b', '', ''),
            ('text.Reset_Handler', '0x0000000008000c7c', '0x48', 'build/startup_stm32f103xb.o', 'b', '', ''),
            ('text.Default_Handler', '0x0000000008000cc4', '0x2', 'build/startup_stm32f103xb.o', 'b', '', ''),
            ('eh_frame', '0x0000000008000d10', '0x0', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('init', '0x0000000008000d10', '0x4', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o', '/', '', '/'),
            ('init', '0x0000000008000d14', '0x8', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o', '/', '', '/'),
            ('fini', '0x0000000008000d1c', '0x4', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o', '/', '', '/'),
            ('fini', '0x0000000008000d20', '0x8', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o', '/', '', '/'),
            ('iplt', '0x0000000008000d28', '0x0', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('rodata.HAL_RCC_GetSysClockFreq.str1.4', '0x0000000008000d28', '0x11', 'build/stm32f1xx_hal_rcc.o', 'b', '', ''),
            ('rodata.AHBPrescTable', '0x0000000008000d3c', '0x10', 'build/system_stm32f1xx.o', 'b', '', ''),
            ('rel.iplt', '0x0000000008000d4c', '0x0', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('init_array', '0x0000000008000d4c', '0x4', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('fini_array', '0x0000000008000d50', '0x4', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('data.uwTickFreq', '0x0000000020000000', '0x1', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('data.uwTickPrio', '0x0000000020000004', '0x4', 'build/stm32f1xx_hal.o', 'b', '', ''),
            ('data.SystemCoreClock', '0x0000000020000008', '0x4', 'build/system_stm32f1xx.o', 'b', '', ''),
            ('igot.plt', '0x000000002000000c', '0x0', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/'),
            ('bss', '0x000000002000000c', '0x1c', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o', '/', '', '/')
        ]

        lib_symbols = [
            ('text.__libc_init_array', '0x0000000008000cc8', '0x48', '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/arm-none-eabi/9.2.1/../../../../arm-none-eabi/lib/thumb/v7-m/nofp/libc_nano.a(lib_a-init.o)', '/', '', '/', '__libc_init_array')
        ]

        common_symbols = [
            ('0x0000000020000028', '0x4', 'build/stm32f1xx_hal.o', 'b', '', '', 'uwTick')
        ]

        fill_symbols = [
            ('0x0000000008000b76', '0x2'),
            ('0x0000000008000cc6', '0x2'),
            ('0x0000000008000d39', '0x3'),
            ('0x0000000020000001', '0x3'),
            ('0x000000002000002c', '0x4'),
            ('0x0000000020000030', '0x200'),
            ('0x0000000020000230', '0x400')
        ]


        self.assertEqual(len(local), len(local_symbols),
                         f'Failed to parse all local symbols ({len(local)}/{len(local_symbols)}).')
        self.assertEqual(len(lib), len(lib_symbols),
                         f'Failed to parse all external (lib) symbols ({len(lib)}/{len(lib_symbols)}).')
        self.assertEqual(len(common), len(common_symbols), 
                         f'Failed to parse all COMMON symbols ({len(common)}/{len(common_symbols)}).')
        self.assertEqual(len(fill), len(fill_symbols),
                         f'Failed to parse all *fill* symbols ({len(fill)}/{len(fill_symbols)}).')

        local_items = len(local_symbols[0])
        lib_items = len(lib_symbols[0])
        common_items = len(common_symbols[0])
        fill_items = len(fill_symbols[0])

        for i in range(len(local_symbols)):
            for j in range(local_items):
                self.assertEqual(local[i][j], local_symbols[i][j],
                                 f'Wrong local symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(lib_symbols)):
            for j in range(lib_items):
                self.assertEqual(lib[i][j], lib_symbols[i][j],
                                 f'Wrong external (lib) symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(common_symbols)):
            for j in range(common_items):
                self.assertEqual(common[i][j], common_symbols[i][j],
                                 f'Wrong COMMON symbol (symbol number {i}, tuple element {j}.')

        for i in range(len(fill_symbols)):
            for j in range(fill_items):
                self.assertEqual(fill[i][j], fill_symbols[i][j],
                                 f'Wrong *fill* symbol (symbol number {i}, tuple element {j}.')

