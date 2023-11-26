# Import some necessary modules
import LexicalSyntax
import sys
import os

#This is the function to parse user input or file content
def parse_input(input_text):
    # Create a parser object named parser from LexicalSyntax module
    parser = LexicalSyntax.Parser()
    # Parse the input text using the parser
    program = parser.parse(input_text)

    # Create a parser_pt object named parser from LexicalSyntax module
    parser_pt = LexicalSyntax.Parser_PT()
    # Parse the input text using the parser
    program_pt = parser_pt.parse(input_text)

    result = "Parse Tree:\n" + str(program) + "\n\nAbstract Syntax Tree:\n" + str(program_pt)

    # Return the parsed program
    return result

# This is the Read-Eval-Print Loop (REPL) function
def repl():
    print('Syntax Analysis:')

    # Accepting user input continuous until the 'exit' is entered
    while True:
        user_input = input('>>> ')
        # Check if the user wants to exit the loop or not
        if user_input.lower() == 'exit':
            break
        # Check if the user wants to input a file
        elif user_input.lower() == 'file':
            # Get the file path from the user
            file_path = input('Enter the path to the .txt file: ')
            try:
                # Try to open and read the file
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    # Parse the content of the file
                    program = parse_input(file_content)
                    print(program)
            except FileNotFoundError:
                print("File not found. Please enter a valid file path.")
        else:
            # Parse the user input
            program = parse_input(user_input)
            print(program)

if __name__ == '__main__':
    # Print the current working directory
    print("Current working directory:", os.getcwd()) 
    # Check if a command-line argument is provided and it is a .txt file
    if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
        try:
            # Try to open and read the file specified in the command-line argument
            with open(sys.argv[1], 'r') as file:
                file_content = file.read()
                # Parse the content of the file
                program = parse_input(file_content)
                print(program)
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
    else:
        # If no command is provided, enter the REPL
        repl()
