from enum import Enum, auto
import re

# Different token types
class TokenType(Enum):
    NUMBER = auto()
    KEYWORD = auto()
    IDENTIFIER = auto()
    LITERAL = auto()
    OPERATOR = auto()
    EQUALS = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    SPACE = auto()
    EOF = auto()

# Regular expressions for token patterns
TOKEN_REGEX = {
    TokenType.NUMBER: r'[1-9]+[0-9]*|0',
    TokenType.KEYWORD: r'import|from|if|elif|else|return|def|break|continue', 
    TokenType.IDENTIFIER: r'[a-zA-Z_]+[a-zA-Z_0-9]*',
    TokenType.LITERAL: r'".*?"',
    TokenType.OPERATOR: r'[+\-*/%]',
    TokenType.EQUALS: r'=',
    TokenType.OPEN_PAREN: r'\(',
    TokenType.CLOSE_PAREN: r'\)',
    TokenType.SPACE: r'[ \t\r\n]',
}

# Token class representing a token with type and value
class Token:
    def __init__(self, type: TokenType, value: str) -> None:
        self.type: TokenType = type
        self.value: str = value
    def __repr__(self):
        return f'{{ {self.type}, {self.value} }}'

# Function to tokenize the input code
def tokenize(code: str) -> list[Token]:
    tokens: list[Token] = []
    match = None

    # Continue processing the code until it is empty
    while code:
        # Try to match the code for each token pattern
        for tokentype, pattern in TOKEN_REGEX.items():
            match = re.match(pattern, code)

            if match:
                value = match.group()
                code = code[len(value):]

                # Skip for the SPACE tokens
                if tokentype == TokenType.SPACE:
                    continue
                # For LITERAL tokens, remove the quotes then add to tokens
                elif tokentype == TokenType.LITERAL:
                    tokens.append(Token(tokentype, value[1:-1]))
                # For KEYWORD tokens, add to tokens
                elif tokentype == TokenType.KEYWORD:
                    tokens.append(Token(tokentype, value))
                else:
                    # For other tokens not mention, add to tokens
                    tokens.append(Token(tokentype, value))
                break

        # If none of match is found, raise an exception
        if match is None:
            raise Exception(__file__, 'Not valid character: ', code[0])

    # Add EOF token to show that it is the end of tokens
    tokens.append(Token(TokenType.EOF, 'EOF'))
    return tokens
