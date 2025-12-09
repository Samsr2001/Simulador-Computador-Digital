from enum import Enum

class Opcode(Enum):
    LOAD = 0x1
    STORE = 0x2
    ADD = 0x3
    SUB = 0x4
    JUMP = 0x5
    JZ = 0x6
    IN = 0x7
    OUT = 0x8
    LOADI = 0x9
    OUTNUM = 0xA
    HALT = 0xF

class Pantallas(Enum):
    DEFAULT = (800, 600)
    BIG = (1024, 768)

class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
