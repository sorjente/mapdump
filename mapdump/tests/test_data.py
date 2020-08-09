#!/usr/bin/env python3


from mapdump.symbol import Symbol


simple_blinky_raw_local_symbols = [
    (
        'isr_vector',
        '0x0000000008000000',
        '0x10c',
        'build/startup_stm32f103xb.o',
        'b',
        '',
        ''
    ),
    (
        'text',
        '0x000000000800010c',
        '0x40',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'text.MX_GPIO_Init',
        '0x000000000800014c',
        '0x50',
        'build/main.o',
        'b',
        '',
        ''
    ),
    (
        'text.SystemClock_Config',
        '0x000000000800019c',
        '0x50',
        'build/main.o',
        'b',
        '',
        ''
    ),
    (
        'text.main',
        '0x00000000080001ec',
        '0x24',
        'build/main.o',
        'b',
        '',
        ''
    ),
    (
        'text.NMI_Handler',
        '0x0000000008000210',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.HardFault_Handler',
        '0x0000000008000212',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.MemManage_Handler',
        '0x0000000008000214',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.BusFault_Handler',
        '0x0000000008000216',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.UsageFault_Handler',
        '0x0000000008000218',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.SVC_Handler',
        '0x000000000800021a',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.DebugMon_Handler',
        '0x000000000800021c',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.PendSV_Handler',
        '0x000000000800021e',
        '0x2',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.SysTick_Handler',
        '0x0000000008000220',
        '0x8',
        'build/stm32f1xx_it.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_MspInit',
        '0x0000000008000228',
        '0x44',
        'build/stm32f1xx_hal_msp.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_InitTick',
        '0x000000000800026c',
        '0x4c',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_Init',
        '0x00000000080002b8',
        '0x24',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_IncTick',
        '0x00000000080002dc',
        '0x18',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_GetTick',
        '0x00000000080002f4',
        '0xc',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_Delay',
        '0x0000000008000300',
        '0x28',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'text.RCC_Delay',
        '0x0000000008000328',
        '0x2c',
        'build/stm32f1xx_hal_rcc.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_RCC_OscConfig',
        '0x0000000008000354',
        '0x410',
        'build/stm32f1xx_hal_rcc.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_RCC_GetSysClockFreq',
        '0x0000000008000764',
        '0x6c',
        'build/stm32f1xx_hal_rcc.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_RCC_ClockConfig',
        '0x00000000080007d0',
        '0x16c',
        'build/stm32f1xx_hal_rcc.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_GPIO_Init',
        '0x000000000800093c',
        '0x220',
        'build/stm32f1xx_hal_gpio.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_GPIO_WritePin',
        '0x0000000008000b5c',
        '0xc',
        'build/stm32f1xx_hal_gpio.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_GPIO_TogglePin',
        '0x0000000008000b68',
        '0xe',
        'build/stm32f1xx_hal_gpio.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_NVIC_SetPriorityGrouping',
        '0x0000000008000b78',
        '0x24',
        'build/stm32f1xx_hal_cortex.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_NVIC_SetPriority',
        '0x0000000008000b9c',
        '0x68',
        'build/stm32f1xx_hal_cortex.o',
        'b',
        '',
        ''
    ),
    (
        'text.HAL_SYSTICK_Config',
        '0x0000000008000c04',
        '0x2c',
        'build/stm32f1xx_hal_cortex.o',
        'b',
        '',
        ''
    ),
    (
        'text.SystemInit',
        '0x0000000008000c30',
        '0x4c',
        'build/system_stm32f1xx.o',
        'b',
        '',
        ''
    ),
    (
        'text.Reset_Handler',
        '0x0000000008000c7c',
        '0x48',
        'build/startup_stm32f103xb.o',
        'b',
        '',
        ''
    ),
    (
        'text.Default_Handler',
        '0x0000000008000cc4',
        '0x2',
        'build/startup_stm32f103xb.o',
        'b',
        '',
        ''
    ),
    (
        'eh_frame',
        '0x0000000008000d10',
        '0x0',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'init',
        '0x0000000008000d10',
        '0x4',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o',
        '/',
        '',
        '/'
    ),
    (
        'init',
        '0x0000000008000d14',
        '0x8',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o',
        '/',
        '',
        '/'
    ),
    (
        'fini',
        '0x0000000008000d1c',
        '0x4',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o',
        '/',
        '',
        '/'
    ),
    (
        'fini',
        '0x0000000008000d20',
        '0x8',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o',
        '/',
        '',
        '/'
    ),
    (
        'iplt',
        '0x0000000008000d28',
        '0x0',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'rodata.HAL_RCC_GetSysClockFreq.str1.4',
        '0x0000000008000d28',
        '0x11',
        'build/stm32f1xx_hal_rcc.o',
        'b',
        '',
        ''
    ),
    (
        'rodata.AHBPrescTable',
        '0x0000000008000d3c',
        '0x10',
        'build/system_stm32f1xx.o',
        'b',
        '',
        ''
    ),
    (
        'rel.iplt',
        '0x0000000008000d4c',
        '0x0',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'init_array',
        '0x0000000008000d4c',
        '0x4',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'fini_array',
        '0x0000000008000d50',
        '0x4',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'data.uwTickFreq',
        '0x0000000020000000',
        '0x1',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'data.uwTickPrio',
        '0x0000000020000004',
        '0x4',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        ''
    ),
    (
        'data.SystemCoreClock',
        '0x0000000020000008',
        '0x4',
        'build/system_stm32f1xx.o',
        'b',
        '',
        ''
    ),
    (
        'igot.plt',
        '0x000000002000000c',
        '0x0',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    ),
    (
        'bss',
        '0x000000002000000c',
        '0x1c',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o',
        '/',
        '',
        '/'
    )
]


simple_blinky_raw_lib_symbols = [
    (
        'text.__libc_init_array',
        '0x0000000008000cc8',
        '0x48',
        '/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/../../../../arm-none-eabi/lib/thumb/v7-m/nofp/libc_nano.a(lib_a-init.o)',
        '/',
        '',
        '/',
        '__libc_init_array'
    )
]


simple_blinky_raw_common_symbols = [
    (
        '0x0000000020000028',
        '0x4',
        'build/stm32f1xx_hal.o',
        'b',
        '',
        '',
        'uwTick'
    )
]


simple_blinky_raw_fill_symbols = [
    (
        '0x0000000008000b76',
        '0x2'
    ),
    (
        '0x0000000008000cc6',
        '0x2'
    ),
    (
        '0x0000000008000d39',
        '0x3'
    ),
    (
        '0x0000000020000001',
        '0x3'
    ),
    (
        '0x000000002000002c',
        '0x4'
    ),
    (
        '0x0000000020000030',
        '0x200'
    ),
    (
        '0x0000000020000230',
        '0x400'
    )
]


simple_blinky_parsed_symbols = [
    Symbol(
        name='isr_vector',
        address=int('0x0000000008000000', 0),
        size=int('0x10c', 0),
        section='isr_vector',
        file='build/startup_stm32f103xb.o'
    ),
    Symbol(
        name='text',
        address=int('0x000000000800010c', 0),
        size=int('0x40', 0),
        section='text',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o'
    ),
    Symbol(
        name='MX_GPIO_Init',
        address=int('0x000000000800014c', 0),
        size=int('0x50', 0),
        section='text',
        file='build/main.o'
    ),
    Symbol(
        name='SystemClock_Config',
        address=int('0x000000000800019c', 0),
        size=int('0x50', 0),
        section='text',
        file='build/main.o'
    ),
    Symbol(
        name='main',
        address=int('0x00000000080001ec', 0),
        size=int('0x24', 0),
        section='text',
        file='build/main.o'
    ),
    Symbol(
        name='NMI_Handler',
        address=int('0x0000000008000210', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='HardFault_Handler',
        address=int('0x0000000008000212', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='MemManage_Handler',
        address=int('0x0000000008000214', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='BusFault_Handler',
        address=int('0x0000000008000216', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='UsageFault_Handler',
        address=int('0x0000000008000218', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='SVC_Handler',
        address=int('0x000000000800021a', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='DebugMon_Handler',
        address=int('0x000000000800021c', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='PendSV_Handler',
        address=int('0x000000000800021e', 0),
        size=int('0x2', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='SysTick_Handler',
        address=int('0x0000000008000220', 0),
        size=int('0x8', 0),
        section='text',
        file='build/stm32f1xx_it.o'
    ),
    Symbol(
        name='HAL_MspInit',
        address=int('0x0000000008000228', 0),
        size=int('0x44', 0),
        section='text',
        file='build/stm32f1xx_hal_msp.o'
    ),
    Symbol(
        name='HAL_InitTick',
        address=int('0x000000000800026c', 0),
        size=int('0x4c', 0),
        section='text',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='HAL_Init',
        address=int('0x00000000080002b8', 0),
        size=int('0x24', 0),
        section='text',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='HAL_IncTick',
        address=int('0x00000000080002dc', 0),
        size=int('0x18', 0),
        section='text',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='HAL_GetTick',
        address=int('0x00000000080002f4', 0),
        size=int('0xc', 0),
        section='text',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='HAL_Delay',
        address=int('0x0000000008000300', 0),
        size=int('0x28', 0),
        section='text',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='RCC_Delay',
        address=int('0x0000000008000328', 0),
        size=int('0x2c', 0),
        section='text',
        file='build/stm32f1xx_hal_rcc.o'
    ),
    Symbol(
        name='HAL_RCC_OscConfig',
        address=int('0x0000000008000354', 0),
        size=int('0x410', 0),
        section='text',
        file='build/stm32f1xx_hal_rcc.o'
    ),
    Symbol(
        name='HAL_RCC_GetSysClockFreq',
        address=int('0x0000000008000764', 0),
        size=int('0x6c', 0),
        section='text',
        file='build/stm32f1xx_hal_rcc.o'
    ),
    Symbol(
        name='HAL_RCC_ClockConfig',
        address=int('0x00000000080007d0', 0),
        size=int('0x16c', 0),
        section='text',
        file='build/stm32f1xx_hal_rcc.o'
    ),
    Symbol(
        name='HAL_GPIO_Init',
        address=int('0x000000000800093c', 0),
        size=int('0x220', 0),
        section='text',
        file='build/stm32f1xx_hal_gpio.o'
    ),
    Symbol(
        name='HAL_GPIO_WritePin',
        address=int('0x0000000008000b5c', 0),
        size=int('0xc', 0),
        section='text',
        file='build/stm32f1xx_hal_gpio.o'
    ),
    Symbol(
        name='HAL_GPIO_TogglePin',
        address=int('0x0000000008000b68', 0),
        size=int('0xe', 0),
        section='text',
        file='build/stm32f1xx_hal_gpio.o'
    ),
    Symbol(
        name='HAL_NVIC_SetPriorityGrouping',
        address=int('0x0000000008000b78', 0),
        size=int('0x24', 0),
        section='text',
        file='build/stm32f1xx_hal_cortex.o'
    ),
    Symbol(
        name='HAL_NVIC_SetPriority',
        address=int('0x0000000008000b9c', 0),
        size=int('0x68', 0),
        section='text',
        file='build/stm32f1xx_hal_cortex.o'
    ),
    Symbol(
        name='HAL_SYSTICK_Config',
        address=int('0x0000000008000c04', 0),
        size=int('0x2c', 0),
        section='text',
        file='build/stm32f1xx_hal_cortex.o'
    ),
    Symbol(
        name='SystemInit',
        address=int('0x0000000008000c30', 0),
        size=int('0x4c', 0),
        section='text',
        file='build/system_stm32f1xx.o'
    ),
    Symbol(
        name='Reset_Handler',
        address=int('0x0000000008000c7c', 0),
        size=int('0x48', 0),
        section='text',
        file='build/startup_stm32f103xb.o'
    ),
    Symbol(
        name='Default_Handler',
        address=int('0x0000000008000cc4', 0),
        size=int('0x2', 0),
        section='text',
        file='build/startup_stm32f103xb.o'
    ),
    Symbol(
        name='init',
        address=int('0x0000000008000d10', 0),
        size=int('0x4', 0),
        section='init',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o'
    ),
    Symbol(
        name='init',
        address=int('0x0000000008000d14', 0),
        size=int('0x8', 0),
        section='init',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o'
    ),
    Symbol(
        name='fini',
        address=int('0x0000000008000d1c', 0),
        size=int('0x4', 0),
        section='fini',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crti.o'
    ),
    Symbol(
        name='fini',
        address=int('0x0000000008000d20', 0),
        size=int('0x8', 0),
        section='fini',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtn.o'
    ),
    Symbol(
        name='HAL_RCC_GetSysClockFreq.str1.4',
        address=int('0x0000000008000d28', 0),
        size=int('0x11', 0),
        section='rodata',
        file='build/stm32f1xx_hal_rcc.o'
    ),
    Symbol(
        name='AHBPrescTable',
        address=int('0x0000000008000d3c', 0),
        size=int('0x10', 0),
        section='rodata',
        file='build/system_stm32f1xx.o'
    ),
    Symbol(
        name='init_array',
        address=int('0x0000000008000d4c', 0),
        size=int('0x4', 0),
        section='init_array',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o'
    ),
    Symbol(
        name='fini_array',
        address=int('0x0000000008000d50', 0),
        size=int('0x4', 0),
        section='fini_array',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o'
    ),
    Symbol(
        name='uwTickFreq',
        address=int('0x0000000020000000', 0),
        size=int('0x1', 0),
        section='data',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='uwTickPrio',
        address=int('0x0000000020000004', 0),
        size=int('0x4', 0),
        section='data',
        file='build/stm32f1xx_hal.o'
    ),
    Symbol(
        name='SystemCoreClock',
        address=int('0x0000000020000008', 0),
        size=int('0x4', 0),
        section='data',
        file='build/system_stm32f1xx.o'
    ),
    Symbol(
        name='bss',
        address=int('0x000000002000000c', 0),
        size=int('0x1c', 0),
        section='bss',
        file='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
             'arm-none-eabi/9.2.1/thumb/v7-m/nofp/crtbegin.o'
    ),

    Symbol(
        name='__libc_init_array',
        address=int('0x0000000008000cc8', 0),
        size=int('0x48', 0),
        section='text',
        file='lib_a-init.o',
        lib='/usr/local/Caskroom/gcc-arm-embedded/9-2019-q4-major/gcc-arm-none-eabi-9-2019-q4-major/bin/../lib/gcc/'\
            'arm-none-eabi/9.2.1/../../../../arm-none-eabi/lib/thumb/v7-m/nofp/libc_nano.a'
    ),

    Symbol(
        name='uwTick',
        address=int('0x0000000020000028', 0),
        size=int('0x4', 0),
        section='COMMON',
        file='build/stm32f1xx_hal.o'
    ),

    Symbol(
        name='*fill*',
        address=int('0x0000000008000b76', 0),
        size=int('0x2', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x0000000008000cc6', 0),
        size=int('0x2', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x0000000008000d39', 0),
        size=int('0x3', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x0000000020000001', 0),
        size=int('0x3', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x000000002000002c', 0),
        size=int('0x4', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x0000000020000030', 0),
        size=int('0x200', 0),
        section='*fill*',
        file=None
    ),
    Symbol(
        name='*fill*',
        address=int('0x0000000020000230', 0),
        size=int('0x400', 0),
        section='*fill*',
        file=None
    )
]
