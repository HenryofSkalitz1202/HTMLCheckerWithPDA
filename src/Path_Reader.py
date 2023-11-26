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