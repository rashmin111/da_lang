import re

# Define the input file name
input_file_name = "file1.txt"

def list_translations_dynamically():
    """
    Reads the file, finds all language tags, and dynamically adds them to a list.
    """
    try:
        with open(input_file_name, 'r', encoding='utf-8') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' was not found.")
        return []

    # Start with an empty list.
    translations_list = []

    # Find all language tags in the format 'lang:word'.
    # The regex pattern r'lang:\w+' searches for the literal string "lang:" followed by one or more word characters.
    # The findall() method returns a list of all matches found in the string.
    language_tags = re.findall(r'lang:\w+', file_content)

    # Dynamically add all found language tags to the list.
    for tag in language_tags:
        translations_list.append(tag)
    
    return translations_list

# Main program flow
translations = list_translations_dynamically()
if translations:
    print("Found the following translations:")
    for tag in translations:
        print(tag)