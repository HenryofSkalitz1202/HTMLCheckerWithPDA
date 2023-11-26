# https://github.com/msindev/PushDown-Automata-Implementation
# https://adityarizki.net/belajarpython-9-operasi-tokenizing-pada-teks-berbahasa-indonesia/

from FileHandler import FileHandler
from Path_Reader import *
from Custom_Splitter import *
import sys

class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        #Retrieve all information
        inputString += 'e'
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState

        print('State\tInput\tStack\tMove')
        for char in inputString:
            #print('Current TOS', currentStackSymbol)
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if (production[1] == ">" and production[2][1] == "/"):
                        print(production[1], production[2][1])
                        self.stack.pop()
                        break
                    if ((production[4] == 'e') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
                    elif (production[4] == production[1]+production[2]):
                        self.stack.append(char)
                    else:
                        self.stack.pop()
                        self.stack.append(production[4])
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))
    

        if(currentState in finalStates):
            print('String accepted by PDA.')
        else:
            print('String rejected by PDA.')

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

    automataFilePath = pda_file_path
    lines = fh.readFile(automataFilePath)
    print('Reading Automata File')
    print('Automata File Successfully Read')

    inputString = read_html(html_file_path).rstrip()
    parsedLines = fh.parseFile(lines)

    target_after_character = []
    target_around_character = ['>', '=', '"']
    modified_html = add_whitespace_around_characters(clear_text_of_all_tags(clear_attributes(inputString)), target_around_character, target_after_character)

    pda.compute(modified_html.split(), parsedLines)

if __name__ == '__main__':
    main()
