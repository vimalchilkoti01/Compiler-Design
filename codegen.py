def codegen(ast):
    code = ["const fs = require('fs');"]
    
    for stmt in ast.statements:
        if stmt.type == 'Source':
            duration_value = stmt.duration['value']
            unit = stmt.duration['unit']
            duration_ms = duration_value * (1000 if unit == 's' else 60000)  
            
            file_path = stmt.file.strip('"')  
            code.append(f"setInterval(() => {{")
            code.append(f"    const data = fs.readFileSync('{file_path}', 'utf8');")
            code.append(f"    data.split('\\n').forEach(line => console.log(line));")
            code.append(f"}}, {duration_ms});")
    
    return '\n'.join(code)

if __name__ == "__main__":
    from lexer import lex
    from parser import Parser
    from semantic import semantic_analysis

    test_code = 'source "website_logs" every 10s emit log_entry;'
    tokens = lex(test_code)
    parser = Parser(tokens)
    ast = parser.parse_program()
    validated_ast = semantic_analysis(ast)
    js_code = codegen(validated_ast)
    print("Generated JavaScript:")
    print(js_code)