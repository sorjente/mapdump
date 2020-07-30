#!/usr/bin/env python3

class Memory(object):
    '''
    Describes a memory sector (like FLASH, RAM etc).
    '''
    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size


    def __str__(self):
        return f"{self.name} @ {self.address:#012x} ({self.size} bytes)"
        
