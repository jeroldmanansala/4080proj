from tokens import TokenType, Token
from error_handler import LexerError

class Lexer:
    def __init__(self, input):
        self.input = input
        self.tokens = []
        self.current_pos = 0

    def lex(self):
        while self.current_pos < len(self.input):
            token_start_pos = self.current_pos
            lookahead = self.input[self.current_pos]

            if lookahead.isspace():
                self.current_pos += 1  # ignore whitespace
            elif lookahead == '=':
                self.tokens.append(Token(TokenType.ASSIGN, '=', token_start_pos))
                self.current_pos += 1
            elif lookahead == ',':
                self.tokens.append(Token(TokenType.SKIP, ',', token_start_pos))
                self.current_pos += 1
            elif lookahead == '(':
                self.tokens.append(Token(TokenType.LPAREN, '(', token_start_pos))
                self.current_pos += 1
            elif lookahead == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')', token_start_pos))
                self.current_pos += 1
            elif lookahead == "'":
                self.current_pos += 1  # Skip the opening quote
                start_quote_pos = self.current_pos
                while self.current_pos < len(self.input) and self.input[self.current_pos] != "'":
                    self.current_pos += 1
                text = self.input[start_quote_pos:self.current_pos]
                self.tokens.append(Token(TokenType.COLOR_NAME, text, start_quote_pos))
                self.current_pos += 1  # Skip the closing quote
            elif lookahead.isdigit():
                num_start = self.current_pos
                while self.current_pos < len(self.input) and self.input[self.current_pos].isdigit():
                    self.current_pos += 1
                number = self.input[num_start:self.current_pos]
                self.tokens.append(Token(TokenType.NUMBER, number, num_start))
            elif lookahead.isalpha() or lookahead == '_':  # Allow underscores in identifiers
                ident_start = self.current_pos
                while self.current_pos < len(self.input) and (self.input[self.current_pos].isalnum() or self.input[self.current_pos] == '_'):
                    self.current_pos += 1
                identifier = self.input[ident_start:self.current_pos]
                if identifier == 'draw_circle':
                    token_type = TokenType.DRAW_CIRCLE
                elif identifier == 'set_color':
                    token_type = TokenType.SET_COLOR
                else:
                    token_type = TokenType.IDENTIFIER
                self.tokens.append(Token(token_type, identifier, ident_start))
            else:
                raise LexerError(f"Unknown character '{lookahead}' at position {self.current_pos}")

        self.tokens.append(Token(TokenType.EOF, '<EOF>', self.current_pos))  # End-of-file marker
        return self.tokens



