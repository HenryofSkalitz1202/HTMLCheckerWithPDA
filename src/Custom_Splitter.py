from bs4 import BeautifulSoup, NavigableString

def clear_attributes(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')

    tags_to_clear = {
        'a': ['href', 'class', 'id', 'style', 'target'],
        'img': ['src', 'alt', 'class', 'id', 'style'],
        'link': ['rel', 'href', 'class', 'id', 'style'],
        'script': ['src', 'class', 'id', 'style'],
        'form': ['action', 'class', 'id', 'style'],
        'div': ['id', 'class', 'style'],
        'input': ['id', 'class', 'style']
    }

    for tag, attributes in tags_to_clear.items():
        for tag_instance in soup.find_all(tag):
            for attribute in attributes:
                if attribute in tag_instance.attrs:
                    tag_instance[attribute] = ''

    modified_html = str(soup)

    modified_html = modified_html.replace('</br>', '<br>').replace('<br/>', '<br>')
    return modified_html

def clear_text_of_all_tags(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')

    def clear_text(tag):
        for child in tag.children:
            if isinstance(child, NavigableString):
                child.replace_with('')
            elif hasattr(child, 'children') and len(child.contents) > 0:
                clear_text(child)

    for tag in soup.find_all():
        clear_text(tag)

    modified_html = str(soup)

    modified_html = modified_html.replace('</br>', '<br>').replace('<br/>', '<br>')
    modified_html = modified_html.replace('</hr>', '<hr>').replace('<hr/>', '<hr>')

    return modified_html

def add_whitespace_around_characters(input_string, around_characters, after_characters):
    result = input_string
    for target_character in after_characters:
        result = result.replace(target_character, f'{target_character} ')
    for target_character in around_characters:
        result = result.replace(target_character, f' {target_character} ')
    for target_character in result:
        result = result.replace('/>', '>')
    return result