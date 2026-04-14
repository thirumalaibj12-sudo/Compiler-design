import re

def lexical_analyzer(input_str):
    # Simple tokenization: identifiers, numbers, operators
    tokens = re.findall(r'\b\w+\b|[+\-*/=()]', input_str)
    return tokens

if __name__ == "__main__":
    with open("inputs/input_lex.txt", "r") as f:
        input_str = f.read()
    tokens = lexical_analyzer(input_str)
    with open("outputs/output_lex.txt", "w") as f:
        for token in tokens:
            f.write(token + "\n")
    print("Lexical analysis complete. Check outputs/output_lex.txt")
