# Lexical and Syntax Analysis
<p>This assignment implements a simple programming language with lexical and syntax analysis. The analysis divides into two primary components:</p>

<ul>
  <li>Lexical Analysis (Lexer): Tokenizes the input code.</li>
  <li>Syntax Analysis (Parser): Constructs an Abstract Syntax Tree (AST) from tokenized code.</li>
</ul>

# Grammar
<p>The following grammar rules define the language syntax.</p>

  >**Program** : Stmt* <br><br>
  >**Stmt** : AdditiveExpr <br><br>
  >**AdditiveExpr** : MultiplicativeExpr((PLUS | MINUS) MultiplicativeExpr)* <br><br>
  >**MultiplicativeExpr** : Factor((MUL | DIV) Factor)* <br><br>
  >**Factor** : INTEGER <br>
  >(Open_Paren) AdditiveExpr (Close_Paren) 
<p>These rules describe the structure of valid programs in the language.</p>

# Project Structure
Here are all the program files in ***Lexical Syntax*** folder

>`lexer.py`: Lexical analysis implementation. <br><br>
>`parser.py`: Syntax analysis implementation. <br><br>
>`ast.py`: Abstract Syntax Tree (AST) classes. <br><br>
>`main.py`: Main program execution. <br><br>
>`grammar.txt`: Grammar rules define for the programming language. <br><br>
>`test.txt`: Example of input file. <br><br>

# Abstract Syntax Tree (AST)
<p>The structure of the parsed code is defined in the AST classes:</p>

>**Program**: Represents the whole program that contains a list of statements. <br><br>
>**Stmt**: Represents a generic statement in the AST. <br><br>
>**BinaryExpr**: Represents a binary expression. <br><br>
>**Factor**: Represents a generic factor in the AST. <br><br>
>**NumberFactor**: A specific type of factor holding an integer value. <br><br>
>**NodeType**: Specifying the type of each AST node. <br><br>

# Example for input data
Please find the sample input file at `test.txt`

# Requirements
<ul>
  <li>Visual Studio Code (or any preferred IDE Python development environment)</li>
</ul>

# Getting Started
## Run the lexical analysis phase
>1. Open your preferred IDE that supports Python programming. 
>2. Load the project by opening the project folder.
>3. Run the program by navigating to the `lexer.py` file in the project directory under ***Lexical Analysis*** folder.
>4. Execute the program `lexer.py` using your IDE.
>5. Enter the regular expression in the console.
>6. The output will be showing the different type of token based on regular expression entered.

## Run the Syntax analysis phase
### Method 1 (Load text file)
>1. Open your preferred IDE that supports Python programming. 
>2. Load the project by opening the project folder.
>3. Run the program by navigating to the `main.py` file in the project directory under ***Lexical Syntax*** folder.
>4. Execute the program `main.py` using your IDE.
>5. To load the text file type in the word _file_ in the console.
>6. Copy and paste the path of the `test.txt` file in the console.
>7. The output is generated for both parse tree and Abstract Syntax Tree (AST).
>8. Enter _exit_ to end the program or file to input the path from a file.

### Method 2 (Enter Command)
>1. Open your preferred IDE that supports Python programming. 
>2. Load the project by opening the project folder.
>3. Run the program by navigating to the `main.py` file in the project directory under ***Lexical Syntax*** folder.
>4. Execute the program `main.py` using your IDE.
>5. Enter basic arithmetic expressions command in the console.
>6. The output is generated for both parse tree and Abstract Syntax Tree (AST).

## Example regular expression
<ul>
  <li>5+7*10-3</li>
  <li>Aplus = 80%(3+2)+"Excellent"</li>
  <li>x = 7+10/2*(2+8)</li>
  <li>&</li>
  <li>final$</li>
  <li>Hello = “Yen San”</li>
</ul>

## Example arithmetic expressions
<ul>
  <li>5+7*10-3</li>
  <li>3+4-6*2</li>
  <li>j=3+r</li>
</ul>

# Contributors
<p>This assignment was developed by the following members</p>
<ol>
  <li>Veytri A/L Yogan</li>
  <li>Lim Yong Xin</li>
  <li>Chan Yee Shuen</li>
  <li>Soh Yen San</li>
  <li>Khausaalyaah A/P Sinathurai</li>
</ol>

# License
<p>This assignment codebase is licensed under the</p>
[MIT License](https://opensource.org/licenses/MIT/)