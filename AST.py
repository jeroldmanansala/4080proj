# File to handle AST and commands

class ASTNode:
    def evaluate(self, context):
        return None

class Assign(ASTNode):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def evaluate(self, context):
        context[self.variable] = int(self.value)
        print(f"Assigned {self.value} to variable '{self.variable}'")


class SetColor(ASTNode):
    def __init__(self, color):
        self.color = color

    def evaluate(self, context):
        context['color'] = self.color
        print(f"Set color to '{self.color}'")


class DrawCircle(ASTNode):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def evaluate(self, context):
        if self.radius in context:
            radius_value = context[self.radius]
        else:
            raise ValueError(f"Variable '{self.radius}' is not defined")
        print(f"Drawing a circle with radius {radius_value} and color '{self.color}'")
