from lexer import TokenType
from AST import Assign, SetColor, DrawCircle
from error_handler import ParserError

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def eat(self):
        self.pos += 1 # update to next token
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        ast_nodes = []

        while self.current_token and self.current_token.type != TokenType.EOF:
            
            if self.current_token.type == TokenType.DRAW_CIRCLE:
                ast_nodes.append(self.parse_draw_circle())
            elif self.current_token.type == TokenType.SET_COLOR:
                ast_nodes.append(self.parse_set_color())
            elif self.current_token.type == TokenType.IDENTIFIER:
                ast_nodes.append(self.parse_assignment())
            else:
                raise ParserError(f"Unexpected token {self.current_token}")

        return ast_nodes

    def parse_draw_circle(self):
        self.eat()  # eat 'draw_circle'
        if self.current_token.type != TokenType.LPAREN:
            raise ParserError("Expected '(' after 'draw_circle'")
        self.eat()  # eat '('

        if self.current_token.type != TokenType.IDENTIFIER:
            raise ParserError("Expected identifier for radius")
        radius = self.current_token.text
        self.eat()  # eat radius

        if self.current_token.type != TokenType.SKIP:
            raise ParserError("Expected ',' after radius")
        self.eat()  # eat ','

        if self.current_token.type != TokenType.COLOR_NAME:
            raise ParserError("Expected color name for draw_circle")
        color = self.current_token.text
        self.eat()  # eat color

        if self.current_token.type != TokenType.RPAREN:
            raise ParserError("Expected ')' after arguments to 'draw_circle'")
        self.eat()  # eat ')'

        return DrawCircle(radius, color)

    def parse_set_color(self):
        self.eat()  # eat 'set_color'
        if self.current_token.type != TokenType.LPAREN:
            raise ParserError("Expected '(' after 'set_color'")
        self.eat()  # eat '('

        if self.current_token.type != TokenType.COLOR_NAME:
            raise ParserError("Expected color name for set_color")
        color = self.current_token.text
        self.eat()  # eat color

        if self.current_token.type != TokenType.RPAREN:
            raise ParserError("Expected ')' after arguments to 'set_color'")
        self.eat()  # eat ')'

        return SetColor(color)

    def parse_assignment(self):
        var_name = self.current_token.text
        self.eat()  # eat identifier

        if self.current_token.type != TokenType.ASSIGN:
            raise ParserError(f"Expected '=' after identifier '{var_name}'")
        self.eat()  # eat '='

        if self.current_token.type != TokenType.NUMBER:
            raise ParserError(f"Expected number after '=' for variable '{var_name}'")
        value = self.current_token.text
        self.eat()  # eat number

        return Assign(var_name, value)



    

