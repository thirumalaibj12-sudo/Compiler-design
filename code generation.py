import re
class CodeGenerator:
    def __init__(self):
        self.operator_stack = []
        self.operand_stack = []
        self.temp_count = 0
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def new_temp(self):
        """Generates a new temporary variable name."""
        self.temp_count += 1
        return f"t{self.temp_count}"
    def generate_instruction(self, op, arg1, arg2):
        """Prints the generated 3-address code instruction."""
        temp_var = self.new_temp()
        print(f"{temp_var} = {arg1} {op} {arg2}")
        return temp_var
    def process_operator(self):
        """Pops an operator and two operands to generate code."""
        if len(self.operand_stack) < 2:
            return
        op = self.operator_stack.pop()
        right = self.operand_stack.pop()
        left = self.operand_stack.pop()
        result_temp = self.generate_instruction(op, left, right)
        self.operand_stack.append(result_temp)
    def parse_and_generate(self, expression):
        print(f"\n--- Generating Code for: {expression} ---")
        print("Generated Instructions:")
        if '=' in expression:
            lhs, rhs = expression.split('=', 1)
            lhs = lhs.strip()
            expression = rhs.strip()
        else:
            lhs = None
        tokens = re.findall(r"\d+|[a-zA-Z_]\w*|[-+*/^()]", expression)
        for token in tokens:
            if token.isalnum(): 
                self.operand_stack.append(token)
            elif token == '(':
                self.operator_stack.append(token)
            elif token == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.process_operator()
                self.operator_stack.pop() 
            elif token in self.precedence:
                while (self.operator_stack and 
                       self.operator_stack[-1] in self.precedence and 
                       self.precedence[self.operator_stack[-1]] >= self.precedence[token]):
                    self.process_operator()
                self.operator_stack.append(token)
        while self.operator_stack:
            self.process_operator()
        if lhs:
            final_result = self.operand_stack.pop()
            print(f"{lhs} = {final_result}")
        print("---------------------------------------")
if __name__ == "__main__":
    generator = CodeGenerator()
    print("Compiler Design: Simple Code Generator")
    print("Enter expressions like: x = a + b * c")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Enter expression: ")
        if user_input.lower() == 'exit':
            break
        try:
            generator.parse_and_generate(user_input)
            generator.temp_count = 0
            generator.operator_stack = []
            generator.operand_stack = []
        except Exception as e:
            print(f"Error parsing expression: {e}")
