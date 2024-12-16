from enum import Enum, auto
# file to hold tokens

class TokenType(Enum):
    DRAW_CIRCLE = auto()
    SET_COLOR = auto()
    COLOR_NAME = auto()
    NUMBER = auto()
    EOF = auto()
    SKIP = auto()
    ASSIGN = auto()
    IDENTIFIER = auto()
    LPAREN = auto()
    RPAREN = auto()
    QUOTE = auto()

class Token:
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos

    def __str__(self):
        return f"Token({self.type.name}, '{self.text}', {self.pos})"
    



