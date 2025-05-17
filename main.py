import sys
from lexer import lex
from parser import Parser
from semantic import semantic_analysis
from codegen import codegen

# Check for input file argument
if len(sys.argv) != 2:
    print("Usage: python main.py <script.es>")
    sys.exit(1)

script_file = sys.argv[1]

# Read the test script
with open(script_file, 'r') as f:
    code = f.read().strip()

# Tokenize
tokens = lex(code)
print("Tokens:", tokens)

# Parse
parser = Parser(tokens)
ast = parser.parse_program()
print("AST:", ast)

# Semantic Analysis
validated_ast = semantic_analysis(ast)
print("Validated AST:", validated_ast)

# Code Generation
js_code = codegen(validated_ast)
print("Generated JavaScript:")
print(js_code)

# Save the generated code
output_file = 'output/output.js'
with open(output_file, 'w') as f:
    f.write(js_code)
print(f"Generated code saved to {output_file}")