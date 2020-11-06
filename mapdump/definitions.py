#!/usr/bin/env python3

VERSION = "1.0.1"

# Memory section name
# Whitespace
# Memory section start address
# Whitespace
# Memory section size
MEMORY_CONFIG_REGEX = r"([a-zA-Z0-9*_]+)"\
                      r"[ \t]+"\
                      r"(0x[a-zA-Z0-9]+)"\
                      r"[ \t]+"\
                      r"(0x[a-zA-Z0-9]+)"

# Section & symbol name
# Whitespace
# Symbol start address
# Whitespace
# Symbol size
# Whitespace
# Path of .o file that contains the symbol
LOCAL_SYMBOL_REGEX = r"\.([a-zA-Z0-9._]+)"\
                     r"[\s]+"\
                     r"(0x[a-zA-Z0-9]+)"\
                     r"[\s]+"\
                     r"(0x[a-zA-Z0-9]+)"\
                     r"[\s]+"\
                     r"(([a-zA-Z]|(\.\/)|(\/))[a-zA-Z0-9\/._-]+\.o)"

# Section name
# Whitespace
# Symbol start address
# Whitespace
# Symbol size
# Whitespace
# Path of .a/.o file that contains the symbol: "<lib>.a(<file>.o)"
# Whitespace
# Symbol start address
# Whitespace
# Symbol name
LIB_SYMBOL_REGEX = r"\.([a-zA-Z0-9._]+)"\
                   r"[\s]+"\
                   r"(0x[a-zA-Z0-9]+)"\
                   r"[\s]+"\
                   r"(0x[a-zA-Z0-9]+)"\
                   r"[\s]+"\
                   r"(([a-zA-Z]|(\.\/)|(\/))[a-zA-Z0-9\/._-]+\.a\([a-zA-Z0-9_-]+\.o\))"\
                   r"[\s]+"\
                   r"0x[a-zA-Z0-9]+"\
                   r"[\s]+"\
                   r"([a-zA-Z0-9_]+)"


# COMMON section
# Whitespace
# Symbol start address
# Whitespace
# Symbol size
# Whitespace
# Path of .o file that contains the symbol
# Whitespace
# Address (same as before)
# Symbol name
COMMON_SYMBOL_REGEX = r"COMMON"\
                      r"[\s]+"\
                      r"(0x[a-zA-Z0-9]+)"\
                      r"[\s]+"\
                      r"(0x[a-zA-Z0-9]+)"\
                      r"[\s]+"\
                      r"(([a-zA-Z]|(\.\/)|(\/))[a-zA-Z0-9\/._-]+\.o)"\
                      r"[\s]+"\
                      r"[a-zA-Z0-9]+"\
                      r"[\s]+"\
                      r"([a-zA-Z0-9_]+)"


# FILL entry
# Whitespace
# Start address
# Whitespace
# Size
FILL_SYMBOL_REGEX = r"\*fill\*"\
                    r"[\s]+"\
                    r"(0x[a-zA-Z0-9]+)"\
                    r"[\s]+"\
                    r"(0x[a-zA-Z0-9]+)"
