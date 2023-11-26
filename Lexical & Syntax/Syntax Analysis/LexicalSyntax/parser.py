from .lexer import Token, TokenType, tokenize
from .ast import BinaryExpr, Factor, NumberFactor, Program, Stmt
from .pt import BinaryExpr_PT, Factor_PT, NumberFactor_PT, Program_PT, Stmt_PT

# AST Parser
class Parser:
    def __init__(self) -> None:
        pass

    def tk(self) -> Token:
        return self.tokens[0]

    def eat(self) -> Token:
        """
        Return the current token and move to the next token
        """
        return self.tokens.pop(0)
  
    def expect(self, tokentype: TokenType) -> Token:
        if self.tk().type == tokentype:
            return self.eat()

        raise Exception(__file__, 'Token expected ', tokentype.name, ' not found. Got ', self.tk(), ' instead.')

    def parse(self, code: str) -> Program:
        # Tokenize the input code
        self.tokens = tokenize(code)

        # Start parsing the program
        return self.parse_program()

    def parse_program(self) -> Program:
        """
        Program -> Stmt*
        """
        # Create an object called program to store the parsed statements
        program = Program()

        # Parse the statements until the end of the input
        while self.tk().type != TokenType.EOF:
            program.body.append(self.parse_stmt())
        return program

    def parse_stmt(self) -> Stmt:
        """
        Stmt -> AdditiveExpr
        """
        # Parse an additive expression as a statement
        return self.parse_additive_expr()

    def parse_additive_expr(self) -> Stmt:
        """
        AdditiveExpr -> MultiplicativeExpr (( PLUS | MINUS ) MultiplicativeExpr)*
        """
        # Parse the first multiplicative expression
        left = self.parse_multiplicative_expr()

        # Continue parsing as long as there are additive operators such as plus or minus
        while self.tk().value == '+' or self.tk().value == '-':
            operator = self.eat().value
            right = self.parse_multiplicative_expr()
            left = BinaryExpr(left, operator, right)
        return left

    def parse_multiplicative_expr(self) -> Stmt:
        """
        MultiplicativeExpr -> Factor (( MUL | DIV ) Factor)*
        """
        # Parse the first factor
        left = self.parse_factor()

        # Continue parsing as long as there are multiplicative operators such as multiply (*) or divide (/)
        while self.tk().value == '*' or self.tk().value == '/':
            operator = self.eat().value
            right = self.parse_factor()
            left = BinaryExpr(left, operator, right)

        return left
  
    def parse_factor(self) -> Stmt:
        """
        Factor -> INTEGER
                | OPEN_PAREN expr CLOSE_PAREN
        """
        # Parse the statement based on the type of token
        if self.tk().type == TokenType.NUMBER:
            # If the token is a numerical value, create a NumberFactor
            return NumberFactor(int(self.eat().value))
        elif self.tk().type == TokenType.OPEN_PAREN:
            # If the token is an open parenthesis, parse an additive expression inside parentheses
            self.eat()
            value = self.parse_additive_expr()
            self.expect(TokenType.CLOSE_PAREN)
            return value
    
        raise Exception(__file__, 'Cannot parse current token.', self.tk())

# Parse Tree
class Parser_PT:
    def __init__(self) -> None:
        pass

    def tk(self) -> Token:
        return self.tokens[0]

    def eat(self) -> Token:
        """
        Return the current token and move to the next token
        """
        return self.tokens.pop(0)
  
    def expect(self, tokentype: TokenType) -> Token:
        if self.tk().type == tokentype:
            return self.eat()

        raise Exception(__file__, 'Token expected ', tokentype.name, ' not found. Got ', self.tk(), ' instead.')

    def parse(self, code: str) -> Program_PT:
        # Tokenize the input code
        self.tokens = tokenize(code)

        # Start parsing the program
        return self.parse_program()

    def parse_program(self) -> Program_PT:
        """
        Program -> Stmt*
        """
        # Create an object called program to store the parsed statements
        program = Program_PT()

        # Parse the statements until the end of the input
        while self.tk().type != TokenType.EOF:
            program.body.append(self.parse_stmt())
        return program

    def parse_stmt(self) -> Stmt_PT:
        """
        Stmt -> AdditiveExpr
        """
        # Parse an additive expression as a statement
        return self.parse_additive_expr()

    def parse_additive_expr(self) -> Stmt_PT:
        """
        AdditiveExpr -> MultiplicativeExpr (( PLUS | MINUS ) MultiplicativeExpr)*
        """
        # Parse the first multiplicative expression
        left = self.parse_multiplicative_expr()

        # Continue parsing as long as there are additive operators such as plus or minus
        while self.tk().value == '+' or self.tk().value == '-':
            operator = self.eat().value
            right = self.parse_multiplicative_expr()
            left = BinaryExpr_PT(left, operator, right)
        return left

    def parse_multiplicative_expr(self) -> Stmt_PT:
        """
        MultiplicativeExpr -> Factor (( MUL | DIV ) Factor)*
        """
        # Parse the first factor
        left = self.parse_factor()

        # Continue parsing as long as there are multiplicative operators such as multiply (*) or divide (/)
        while self.tk().value == '*' or self.tk().value == '/':
            operator = self.eat().value
            right = self.parse_factor()
            left = BinaryExpr_PT(left, operator, right)

        return left
  
    def parse_factor(self) -> Stmt_PT:
        """
        Factor -> INTEGER
                | OPEN_PAREN expr CLOSE_PAREN
        """
        # Parse the statement based on the type of token
        if self.tk().type == TokenType.NUMBER:
            # If the token is a numerical value, create a NumberFactor
            return NumberFactor_PT(int(self.eat().value))
        elif self.tk().type == TokenType.OPEN_PAREN:
            # If the token is an open parenthesis, parse an additive expression inside parentheses
            self.eat()
            value = self.parse_additive_expr()
            self.expect(TokenType.CLOSE_PAREN)
            return value
    
        raise Exception(__file__, 'Cannot parse current token.', self.tk())
