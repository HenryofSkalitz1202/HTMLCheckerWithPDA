from FileHandler import FileHandler
from Path_Reader import read_html
from Custom_Splitter import clear_attributes, clear_text_of_all_tags, add_whitespace_around_characters
import sys
import time

class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        inputString += 'e'
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState

        for elmt in inputString:
            for production in productions:
                if ((production[0] == currentState) and (production[1] == elmt) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if(len(production[4]) == 2):
                        self.stack.append(elmt)
                    elif(len(production[4]) == 3):
                        self.stack.append(elmt)
                        self.stack.append(elmt)
                    elif ((production[4] == 'e') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]

        if(currentState in finalStates):
            print('Accepted')
        else:
            print('Syntax Error')

def main():
    fh = FileHandler()
    pda = PDA()
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python program.py file_html pda_file")
        sys.exit(1)

    # Get file paths from command line arguments
    html_file_path = sys.argv[1]
    pda_file_path = sys.argv[2]

    print('Reading HTML File...')
    html_content = read_html(html_file_path)
    time.sleep(2)
    print('HTML File Successfully Read')
    time.sleep(2)

    lines = fh.readFile(pda_file_path)
    print('Reading Automata File...')
    time.sleep(2)
    print('Automata File Successfully Read')
    time.sleep(2)

    target_after_character = []
    target_around_character = ['>', '=', '"']
    modified_html = add_whitespace_around_characters(clear_text_of_all_tags(clear_attributes(html_content)), target_around_character, target_after_character)
    print('Loading Details from Automata File: ')
    print('========================================')
    time.sleep(3)

    parsedLines = fh.parseFile(lines)
    print('States: ', parsedLines['states'])
    print('Input Symbols: ', parsedLines['input_symbols'])
    print('Stack Symbols: ', parsedLines['stack_symbols'])
    print('Initial State: ', parsedLines['initial_state'])
    print('Initial Stack Symbol: ', parsedLines['initial_stack'])
    print('Final States: ', parsedLines['final_states'])
    print('Productions List:')
    for production in parsedLines['productions']:
        print('\t', production)

    print('Details loaded')
    print('Computing the Transition Table....\n')
    pda.compute(modified_html.split(), parsedLines)

if __name__ == '__main__':
    main()
