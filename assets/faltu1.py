import re

def extract_chapters_with_accurate_labels(input_file, languages):
    """
    Extracts chapters from a single text file into separate files,
    using a pattern-based approach to accurately label each language.

    Args:
        input_file (str): The name of the input file containing all chapters.
        languages (list): A list of languages from the prompt's context.
    """
    current_chapter_number = None
    output_file = None
    
    # Map specific chapter header patterns to their corresponding languages.
    language_patterns = {
        'english': re.compile(r'^(Chapter|ch\.)\s*(\d+)', re.IGNORECASE),
        'albanian': re.compile(r'^(Kapitulli)\s*(\d+)', re.IGNORECASE),
        'arabic': re.compile(r'^(الفصل)\s*(\d+)', re.IGNORECASE), # Al-Fasl
        'bulgarian': re.compile(r'^(Глава)\s*(\d+)', re.IGNORECASE), # Glava
        'chinese': re.compile(r'^(第)\s*(\d+)\s*(章)', re.IGNORECASE), # Di...zhang
        'croatian': re.compile(r'^(Poglavlje)\s*(\d+)', re.IGNORECASE),
        'czech': re.compile(r'^(Kapitola)\s*(\d+)', re.IGNORECASE),
        'estonian': re.compile(r'^(Peatükk)\s*(\d+)', re.IGNORECASE),
        'finnish': re.compile(r'^(Luku)\s*(\d+)', re.IGNORECASE),
        'french': re.compile(r'^(Chapitre)\s*(\d+)', re.IGNORECASE),
        'georgian': re.compile(r'^(თავი)\s*(\d+)', re.IGNORECASE), # Tavi
        'german': re.compile(r'^(Kapitel)\s*(\d+)', re.IGNORECASE),
        'greek': re.compile(r'^(Κεφάλαιο)\s*(\d+)', re.IGNORECASE), # Kefálaio
        'hungarian': re.compile(r'^(\d+\.\s*fejezet)', re.IGNORECASE),
        'indonesian': re.compile(r'^(Bab)\s*(\d+)', re.IGNORECASE),
        'italian': re.compile(r'^(Capitolo)\s*(\d+)', re.IGNORECASE),
        'kazakh': re.compile(r'^(Тарау)\s*(\d+)', re.IGNORECASE), # Tarau
        'korean': re.compile(r'^(제)\s*(\d+)\s*(장)', re.IGNORECASE), # Je...jang
        'latvian': re.compile(r'^(Nodaļa)\s*(\d+)', re.IGNORECASE),
        'malay': re.compile(r'^(Bab)\s*(\d+)', re.IGNORECASE),
        'polish': re.compile(r'^(Rozdział)\s*(\d+)', re.IGNORECASE),
        'portuguese': re.compile(r'^(Capítulo)\s*(\d+)', re.IGNORECASE),
        'romanian': re.compile(r'^(Capitolul)\s*(\d+)', re.IGNORECASE),
        'serbian': re.compile(r'^(Поглавље)\s*(\d+)', re.IGNORECASE), # Poglavlje
        'slovak': re.compile(r'^(Kapitola)\s*(\d+)', re.IGNORECASE),
        'slovenian': re.compile(r'^(Poglavje)\s*(\d+)', re.IGNORECASE),
        'spanish': re.compile(r'^(Capítulo)\s*(\d+)', re.IGNORECASE),
        'swahili': re.compile(r'^(Sura)\s*(\d+)', re.IGNORECASE),
        'turkish': re.compile(r'^(Bölüm)\s*(\d+)', re.IGNORECASE),
        'ukrainian': re.compile(r'^(Розділ)\s*(\d+)', re.IGNORECASE), # Rozdil
        # Fallback for simple number headers
        'number_only': re.compile(r'^\s*(\d+)\s*$')
    }

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                found_match = False
                for lang_name, pattern in language_patterns.items():
                    chapter_match = pattern.search(line)
                    if chapter_match:
                        # Extract the chapter number
                        try:
                            # Chinese and Korean patterns have a different group for the number
                            if lang_name in ['chinese', 'korean']:
                                chapter_number = int(chapter_match.group(2))
                            elif lang_name == 'hungarian':
                                chapter_number = int(chapter_match.group(1).split('.')[0])
                            else:
                                chapter_number = int(chapter_match.group(2))
                        except (ValueError, IndexError):
                            continue
                        
                        # Logic to handle different chapter numbers and file output
                        if chapter_number != current_chapter_number:
                            if output_file:
                                output_file.close()
                            
                            current_chapter_number = chapter_number
                            output_filename = f'chapter{current_chapter_number}.txt'
                            output_file = open(output_filename, 'a', encoding='utf-8')
                            print(f"Adding content to {output_filename}...")
                        
                        # Write the accurate language label
                        if output_file:
                            output_file.write(f'lang:{lang_name.capitalize()}\n')
                        
                        found_match = True
                        break  # Exit the loop once a match is found
                
                # Write the current line to the chapter file if a match was found
                if found_match and output_file and current_chapter_number is not None:
                    output_file.write(line)

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    
    finally:
        if output_file:
            output_file.close()

# List of languages from the prompt
languages_list = [
    "English", "Albanian", "Arabic", "Bulgarian", "Chinese", "Croatian",
    "Czech", "Estonian", "Finnish", "French", "Georgian", "German",
    "Greek", "Hungarian", "Indonesian", "Italian", "Kazakh", "Korean",
    "Latvian", "Malay", "Polish", "Portuguese", "Romanian", "Serbian",
    "Slovak", "Slovenian", "Spanish", "Swahili", "Turkish", "Ukrainian"
]

# Run the function with the more comprehensive patterns
extract_chapters_with_accurate_labels('file1.txt', languages_list)