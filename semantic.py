import os

def semantic_analysis(ast):
    for stmt in ast.statements:
        if stmt.type == 'Source':
            # Check if the file exists
            file_path = stmt.file.strip('"')  # Remove quotes from "website_logs"
            if not os.path.exists(file_path):
                raise Exception(f"Semantic Error: File '{file_path}' does not exist")
            
            # Check if the duration is positive
            duration = stmt.duration['value']
            if duration <= 0:
                raise Exception(f"Semantic Error: Duration must be positive, got {duration}")
        
        elif stmt.type == 'Emit':
            # For now, just ensure the identifier is non-empty
            identifier = stmt.identifier
            if not identifier:
                raise Exception(f"Semantic Error: Emit identifier cannot be empty")

    return ast  # Return the validated AST

if __name__ == "__main__":
    from lexer import lex
    from parser import Parser

    # Test semantic analysis
    test_code = 'source "website_logs" every 10s emit log_entry;'
    tokens = lex(test_code)
    parser = Parser(tokens)
    ast = parser.parse_program()
    validated_ast = semantic_analysis(ast)
    print("Semantic Analysis Passed:", validated_ast)