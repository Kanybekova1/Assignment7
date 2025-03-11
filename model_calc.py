import ast

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char):
        self.expression=self.expression +char

    def remove_last_character(self):
        if self.expression:
            self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {})
            self.expression = str(result)
            return self.expression
        except ZeroDivisionError:
            self.expression = ""
            return "Error"
        except Exception:
            self.expression = ""
            return "Error"
            

    def get_expression(self):
        return self.expression

    def __str__(self):
        return self.expression
