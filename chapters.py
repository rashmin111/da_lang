import re

# Define the input file name
input_file_name = "file1.txt"

# A comprehensive mapping of all "Chapter" translations to their keywords.
CHAPTER_KEYWORDS = {
    "English": "Chapter", "Albanian": "Kapitulli", "Arabic": "الفصل",
    "Bulgarian": "Глава", "Chinese": "章", "Croatian": "Poglavlje",
    "Czech": "Kapitola", "Estonian": "Peatükk", "Finnish": "Luku",
    "French": "Chapitre", "Georgian": "თავი", "German": "Kapitel",
    "Greek": "Κεφάλαιο", "Hungarian": "fejezet", "Indonesian": "Bab",
    "Italian": "Capitolo", "Kazakh": "бөлім", "Korean": "장",
    "Latvian": "Nodaļa", "Malay": "Bab", "Polish": "Rozdział",
    "Portuguese": "Capítulo", "Romanian": "Capitolul", "Russian": "Глава",
    "Serbian": "Поглавље", "Slovak": "Kapitola", "Slovenian": "Poglavje",
    "Spanish": "Capítulo", "Swahili": "Sura ya", "Turkish": "Bölüm",
    "Ukrainian": "Глава",
}

# The explicit list of 30 languages to maintain order.
LANGUAGE_ORDER = [
    "English", "Albanian", "Arabic", "Bulgarian", "Chinese", "Croatian",
    "Czech", "Estonian", "Finnish", "French", "Georgian", "German",
    "Greek", "Hungarian", "Indonesian", "Italian", "Kazakh", "Korean",
    "Latvian", "Malay", "Polish", "Portuguese", "Romanian", "Russian",
    "Serbian", "Slovak", "Slovenian", "Spanish", "Swahili", "Turkish",
    "Ukrainian"
]

def generate_chapter_title_patterns(lang):
    """Generates regex patterns for chapter titles for a given language."""
    patterns = []
    if lang == "Chinese":
        chinese_numbers = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六"}
        for num_int, num_char in chinese_numbers.items():
            patterns.append(re.escape(f"第{num_char}{CHAPTER_KEYWORDS[lang]}"))
    elif lang in ["Hungarian", "Kazakh"]:
        for i in range(1, 7):
            patterns.append(re.escape(f"{i}. {CHAPTER_KEYWORDS[lang]}"))
    else:
        for i in range(1, 7):
            if lang == "Swahili":
                patterns.append(re.escape(f"{CHAPTER_KEYWORDS[lang]} {i}"))
            else:
                patterns.append(re.escape(f"{CHAPTER_KEYWORDS[lang]} {i}"))
    return "|".join(patterns)

def extract_content():
    """Extracts and cleans content for all chapters and languages from the file."""
    try:
        with open(input_file_name, 'r', encoding='utf-8') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file_name}' was not found.")
        return None

    # Prepend 'lang:English' to standardize the first language block.
    if not file_content.strip().startswith('lang:'):
        processed_content = "lang:English\n" + file_content
    else:
        processed_content = file_content

    # Split the entire text file into individual language blocks.
    lang_blocks = re.split(r'lang:(\w+)', processed_content)[1:]
    chapters_by_lang = {i: {} for i in range(1, 7)}
    
    for i in range(0, len(lang_blocks), 2):
        current_lang = lang_blocks[i].strip()
        content_block = lang_blocks[i+1]
        
        if current_lang not in CHAPTER_KEYWORDS:
            continue
            
        # Build the regex to find all chapter titles for the current language
        chapter_title_pattern = generate_chapter_title_patterns(current_lang)
        # Add a pattern to capture any punctuation (like a semicolon) or whitespace
        title_with_punc_pattern = rf"({chapter_title_pattern})[:;]?[\s\n]*"
        
        # Split the content block by the chapter titles to isolate each chapter's content
        chapter_splits = re.split(title_with_punc_pattern, content_block, flags=re.MULTILINE)
        
        # The split results in a list where odd indices are titles and even indices are content.
        # We process them in pairs.
        chapter_num = 1
        for j in range(1, len(chapter_splits), 2):
            content = chapter_splits[j+1].strip()
            if content and chapter_num <= 6:
                chapters_by_lang[chapter_num][current_lang] = content
            chapter_num += 1

    return chapters_by_lang

def write_files(chapters_data):
    """
    Writes the extracted chapter and language data to separate files, maintaining order.
    """
    if chapters_data is None:
        return

    for chapter_num, langs in sorted(chapters_data.items()):
        filename = f"chapter{chapter_num}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for lang in LANGUAGE_ORDER:
                if lang in langs and langs[lang]:
                    f.write(f"lang:{lang}\n\n")
                    f.write(langs[lang] + "\n\n")
        print(f"Successfully created {filename} with {len(langs)} translations.")

# Main program flow
extracted_data = extract_content()
write_files(extracted_data)