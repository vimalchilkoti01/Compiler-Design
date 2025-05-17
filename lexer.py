import re

tokens = [
    (r'\s+', None),  # Whitespace (ignore)
    (r'source|emit|every', 'KEYWORD'),
    (r'"[^"]*"', 'STRING'),
    (r'\d+', 'NUMBER'),
    (r's|m', 'UNIT'),
    (r'[a-zA-Z]\w*', 'IDENTIFIER'),
    (r';', 'SEMICOLON'),
]

def lex(code):
    pos = 0
    token_list = []
    while pos < len(code):
        match = None
        for pattern, token_type in tokens:
            regex = re.compile(pattern)
            match = regex.match(code, pos)  # Match at the current position
            if match:
                if token_type:  # If token_type is not None, add a token
                    token_list.append((token_type, match.group(0)))
                pos = match.end()
                break
        if not match:
            raise Exception(f"Invalid character at position {pos}: '{code[pos]}'")
    return token_list

if __name__ == "__main__":
    
    print(tokens)