import os
import re

# --- CONFIGURATION ---
# Replace with the path to your main input file
input_file_path = 'file1.txt'

# The folder where the new files will be saved
output_folder = 'separated_languages'
# ---------------------

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

try:
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # The regex pattern finds 'lang:tag' and captures all the text that follows,
    # until it finds the next 'lang:' or reaches the end of the file.
    # The re.DOTALL flag is crucial as it allows '.' to match newlines.
    pattern = re.compile(r'(lang:[A-Za-z]+)(.*?)(?=lang:|\Z)', re.DOTALL)
    
    # Find all matches in the content
    matches = pattern.finditer(content)

    if not matches:
        print("No language tags found in the file.")
    
    for match in matches:
        language_tag = match.group(1) # e.g., 'lang:Albanian'
        language_text = match.group(2).strip() # The text for that language
        
        # Create a clean filename from the tag (e.g., 'Albanian.txt')
        language_name = language_tag.split(':')[1]
        output_filename = f"{language_name}.txt"
        output_path = os.path.join(output_folder, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(language_text)
            
        print(f"Successfully saved text for {language_name} to {output_path}")

except FileNotFoundError:
    print(f"Error: The file at '{input_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")