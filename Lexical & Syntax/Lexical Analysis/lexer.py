from enum import Enum, auto
import re

# Different token types for Enum
class TokenType(Enum):
    NUMBER = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    STRING_LITERAL = auto()
    OPERATOR = auto()
    EQUALS = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    SPACE = auto()
    EOF = auto()

# Regular expressions for each type of token
TOKEN_REGEX = {
    TokenType.NUMBER: r'[1-9]+[0-9]*|0',
    TokenType.KEYWORD: r'import|from|if|elif|else|return|def|break|continue',
    TokenType.IDENTIFIER: r'[a-zA-Z_]+[a-zA-Z_0-9]*',
    TokenType.STRING_LITERAL: r'".*?"',
    TokenType.OPERATOR: r'[+\-*/%]',
    TokenType.EQUALS: r'=',
    TokenType.OPEN_PAREN: r'\(',
    TokenType.CLOSE_PAREN: r'\)',
    TokenType.SPACE: r'[ \t\r]',
}

# Class 'Token' represent a token with their type and value
class Token:
    def __init__(self, type: TokenType, value: str) -> None:
        self.type: TokenType = type
        self.value: str = value

    def __repr__(self):
        return f'{{ {self.type}, {self.value} }}'

# Function call to tokenize input code
def tokenize(code: str) -> list[Token]:
    tokens: list[Token] = []
    match = None

    # Continue processing the code until it's empty
    while code:
        # Iterate through token types and try to match the code with patterns
        for tokentype, pattern in TOKEN_REGEX.items():
            match = re.match(pattern, code)

            if match:
                value = match.group()
                code = code[len(value):]

                # Skip the SPACE tokens
                if tokentype == TokenType.SPACE:
                    continue
                # For STRING_LITERAL tokens, remove the quotes and add to tokens
                elif tokentype == TokenType.STRING_LITERAL:
                    tokens.append(Token(tokentype, value[1:-1]))
                # For KEYWORD tokens, add to tokens
                elif tokentype == TokenType.KEYWORD:
                    tokens.append(Token(tokentype, value))
                else:
                    # For other tokens not mentioned, add to tokens
                    tokens.append(Token(tokentype, value))
                break

        # If none of the match is found, raise an exception
        if match is None:
            raise Exception(__file__, 'Not valid character: ', code[0])

    return tokens

# Main loop for lexical analysis
print('Lexical Analysis:')
while True:
    code = input('>>> ')
    tokens = tokenize(code)
    for token in tokens:
        print(token)
