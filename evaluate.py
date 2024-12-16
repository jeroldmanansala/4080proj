from error_handler import EvaluatorError

class Evaluator:
    def __init__(self):
        self.context = {}

    def evaluate(self, ast_nodes):
        for node in ast_nodes:
            try:
                node.evaluate(self.context)
            except EvaluatorError as e:
                print(f"Error while evaluating node {node}: {e}")


