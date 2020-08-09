#!/usr/bin/env python3

from .memory import Memory


class Symbol(object):
    '''
    Describes symbols found in object files.
    '''
    def __init__(self, name, address, size, section, file, lib=None):
        self.name = name
        self.address = address
        self.size = size
        self.section = section
        self.file = file
        self.lib = lib


    def __str__(self):
        return f"{self.name} @ {self.address:#012x} ({self.size} bytes) [{self.file}]"


    def is_in_memory(self, memory):
        return self.address >= memory.address and (self.address + self.size) <= (memory.address + memory.size)


    def is_external(self):
        return self.lib != None


    def is_common(self):
        return self.section == 'COMMON'


    def is_fill(self):
        return self.name == '*fill*'
