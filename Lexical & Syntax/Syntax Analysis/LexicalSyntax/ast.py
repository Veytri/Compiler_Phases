from enum import Enum, auto

# Abstract Syntax Tree
# Different node types for Enum
class NodeType(Enum):
    PROGRAM = auto()
    STMT = auto()
    FACTOR = auto()
    BINARY_EXPR = auto()
    NUMBER_FACTOR = auto()

# Representation of class for the overall program
class Program:
    def __init__(self) -> None:
        self.type: NodeType = NodeType.PROGRAM
        self.body: list[Stmt] = []

    def __repr__(self) -> str:
        res = '{'
        res += '\n\t' + self.type.name

        # Represent each statement in the program
        for stmt in self.body:
            res += '\n' + stmt.__repr__(1)

        res += '\n}'
        return res

# Base class for statements
class Stmt:
    def __init__(self) -> None:
        self.type: NodeType = NodeType.STMT

    def __repr__(self, indent) -> str:
        res = indent * '\t' + self.type.name
        return res

# Binary expressions for class representation
class BinaryExpr(Stmt):
    def __init__(self, left: Stmt, operator: str, right: Stmt) -> None:
        self.type: NodeType = NodeType.BINARY_EXPR
        self.left: Stmt = left
        self.operator: str = operator
        self.right: Stmt = right

    def __repr__(self, indent) -> str:
        res = indent * '\t' + '{'
        res += '\n' + (indent + 1) * '\t' + self.type.name
        res += '\n' + self.left.__repr__(indent + 1)
        res += '\n' + (indent + 1) * '\t' + self.operator
        res += '\n' + self.right.__repr__(indent + 1)
        res += '\n' + indent * '\t' + '}'
        return res

# Base class for representing factor
class Factor(Stmt):
    def __init__(self) -> None:
        self.type: NodeType = NodeType.FACTOR

# Class that representing number factors
class NumberFactor(Factor):
    def __init__(self, value: int) -> None:
        self.type: NodeType = NodeType.NUMBER_FACTOR
        self.value: int = value

    def __repr__(self, indent) -> str:
        return indent * '\t' + f'{{ {self.type.name}, {self.value} }}'
