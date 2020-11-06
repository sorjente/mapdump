# mapdump

Mapdump is a simple command-line tool that analyzes binaries to examine memory usage. It is built mainly for embedded
C code.

## installation

You can download & install `mapdump` via `pip`:

```text
$ pip3 install mapdump
```

You can also download and use `mapdump` by cloning this repo:

```text
$ git clone https://github.com/sorjente/mapdump
$ cd mapdump/
$ python3 -m mapdump <my_binarys_map.map>
```

## usage

_Note: custom options coming soon!_

Using `mapdump` is very simple; you only need to provide it with the `.map` file corresponding to the binary you want
to analyze. Let's say I want to analyse `hello_world.map`:

```text
$ mapdump hello_world.map
FLASH @ 0x0008000000 (524288 bytes)
****************************************
    build/startup_stm32l452.o                                                                                     [460 bytes, 31.94% of FLASH space used]
    lib_a-memcpy.o (/usr/lib/gcc/arm-none-eabi/6.3.1/../../../arm-none-eabi/lib/thumb/v7e-m/fpv4-sp/hard/libc.a)  [308 bytes, 21.39% of FLASH space used]
    rcc.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                                 [220 bytes, 15.28% of FLASH space used]
    lib_a-memset.o (/usr/lib/gcc/arm-none-eabi/6.3.1/../../../arm-none-eabi/lib/thumb/v7e-m/fpv4-sp/hard/libc.a)  [156 bytes, 10.83% of FLASH space used]
    build/main.o                                                                                                  [116 bytes, 8.06% of FLASH space used]
    gpio_common_f0234.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                   [68 bytes, 4.72% of FLASH space used]
    flash_common_all.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                    [36 bytes, 2.50% of FLASH space used]
    flash_common_idcache.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                [32 bytes, 2.22% of FLASH space used]
    rcc_common_all.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                      [26 bytes, 1.81% of FLASH space used]
    gpio_common_all.o (./libopencm3/lib/libopencm3_stm32l4.a)                                                     [18 bytes, 1.25% of FLASH space used]
```


## dev notes

Tests can (and should be!) run with the following command:

```bash
$ python3 -m unittest discover -s mapdump/tests
```
