class Node:
    def __init__(self, type, **kwargs):
        self.type = type
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{self.type}({', '.join(f'{k}={v}' for k, v in self.__dict__.items() if k != 'type')})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type, expected_value=None):
        token = self.peek()
        if not token:
            raise Exception("Unexpected end of input")
        token_type, token_value = token
        if token_type != expected_type or (expected_value and token_value != expected_value):
            raise Exception(f"Expected {expected_type} {expected_value or ''}, got {token}")
        self.pos += 1
        return token

    def parse_program(self):
        statements = []
        while self.peek():
            statements.append(self.parse_statement())
            if self.peek() and self.peek()[0] == 'SEMICOLON':
                self.consume('SEMICOLON')
        return Node('Program', statements=statements)

    def parse_statement(self):
        token = self.peek()
        if token[0] == 'KEYWORD' and token[1] == 'source':
            return self.parse_source()
        elif token[0] == 'KEYWORD' and token[1] == 'emit':
            return self.parse_emit()
        raise Exception(f"Invalid statement: {token}")

    def parse_source(self):
        self.consume('KEYWORD', 'source')
        file = self.consume('STRING')[1]  # Get the string value (e.g., "website_logs")
        self.consume('KEYWORD', 'every')
        number = int(self.consume('NUMBER')[1])  # Get the number (e.g., 10)
        unit = self.consume('UNIT')[1]  # Get the unit (e.g., 's')
        duration = {'value': number, 'unit': unit}
        return Node('Source', file=file, duration=duration)

    def parse_emit(self):
        self.consume('KEYWORD', 'emit')
        identifier = self.consume('IDENTIFIER')[1]  # Get the identifier (e.g., log_entry)
        return Node('Emit', identifier=identifier)

if __name__ == "__main__":
    from lexer import lex
    test_code = 'source "website_logs" every 10s emit log_entry;'
    tokens = lex(test_code)
    parser = Parser(tokens)
    ast = parser.parse_program()
    print(ast)