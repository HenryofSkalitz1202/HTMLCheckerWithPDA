import sys

# Check if correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python program.py file_html pda_file")
    sys.exit(1)

# Get file paths from command line arguments
html_file_path = sys.argv[1]
pda_file_path = sys.argv[2]

def read_html(html_file_path):
    try:
    # Read HTML file
        with open(html_file_path, 'r') as html_file:
            html_content = html_file.read()
            return html_content
    except Exception as e:
        print("An error occurred while reading HTML file:", e)

def read_pda(pda_file_path):
    try:
        # Read PDA file
        with open(pda_file_path, 'r') as pda_file:
            pda_content = pda_file.read()
            return pda_content
    except Exception as e:
        print("An error occurred while reading PDA file:", e)