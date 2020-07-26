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


def main():
    print(get_memory_config("../../embedded/custom-pcb/hello_opencm3/build/main.map"))
    print(construct_memory_dict(get_raw_symbols("../../embedded/custom-pcb/hello_opencm3/build/main.map")))

if __name__ == "__main__":
    main()
