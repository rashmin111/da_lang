import re

# --- CONFIGURATION ---
# Replace with the path to your input file
input_file_path = 'file1.txt'

# The name of the output file
output_file_name = 'file.lang.txt'
# ---------------------

def extract_language_tags(file_path):
    """
    Reads a file, finds all unique language tags, and returns them as a sorted list.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # The regex pattern finds 'lang:' followed by one or more letters.
            # This handles tags like 'lang:Albanian', 'lang:French', etc.
            language_tags = re.findall(r'lang:[A-Za-z]+', content)
            
            # Use a set to get only unique tags, then sort them
            unique_tags = sorted(list(set(language_tags)))
            return unique_tags
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_tags_to_file(tags, output_path):
    """
    Saves a list of strings to a new file, one item per line.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for tag in tags:
                f.write(tag + '\n')
        print(f"Successfully saved {len(tags)} unique language tags to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Main execution block
if __name__ == "__main__":
    extracted_tags = extract_language_tags(input_file_path)
    if extracted_tags:
        save_tags_to_file(extracted_tags, output_file_name)
