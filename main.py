from lexer import Lexer
from parser import Parser
from evaluate import Evaluator

# Language theme is based on art
# Includes variable assignments and error handling
# Could not get loops working :(
# draw_circle command that takes a radius and color param
# set_color command that takes a color param

def main():
    # Test cases
    code = """
    radius = 100
    draw_circle(radius, 'red')
    set_color('pink')
    """

    lexer = Lexer(code)
    tokens = lexer.lex()
    print("Tokens:")
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    commands = parser.parse()
    print("\nParsed Commands:")
    for command in commands:
        print(command)

    evaluator = Evaluator()
    print("\nEvaluation:")
    evaluator.evaluate(commands)

if __name__ == "__main__":
    main()
