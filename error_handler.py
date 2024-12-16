# File to handle different types of errors

class LexerError:
    def __init__(self, message, position):
        self.message = message
        self.position = position
        super().__init__(f"Lexer Error: {message} at position {position}")

class ParserError:
    def __init__(self, message, token):
        self.message = message
        self.token = token
        super().__init__(f"Parser Error: {message} near '{token.text}' at position {token.pos}")

class EvaluatorError:
    def __init__(self, message):
        self.message = message
        super().__init__(f"Runtime Error: {message}")
