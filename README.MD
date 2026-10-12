# 📚 Multilingual Text Segmenter & Restructurer

A Python-based **text processing and analytics pipeline** designed to ingest unorganized, multi-language translated text files, isolate the content chapter by chapter, and programmatically restructure the text into a clean, readable layout.

## 🚀 How It Works
The script **`chapters.py`** processes raw, chaotic files containing blended translations from the `da_lang/assets/` directory. It uses pattern matching and structural parsing to slice the text chapter by chapter, rearrange the structural layout based on specific formatting rules, and output a highly organized, plain text file named **`file1.txt`**.

---

## 📂 Project Structure

```text
├── da_lang/
│   └── assets/           # Experimental and raw, unorganized multi-language text files
├── chapters.py           # Core pipeline script (executes segmentation and layout restructuring)
├── file1.txt             # Structured, chapter-isolated output plain-text file
└── README.md             # Project documentation
```

---

## 🛠️ Features & Workflow

*   **Translation Splitting:** Automatically detects and handles multiple language translations mixed within single raw assets.
*   **Chapter Extraction:** Isolates raw text into distinct chapters using custom text-parsing boundaries.
*   **Custom Layout Restructuring:** Dynamically rearranges structural text components into a uniform, customized arrangement.
*   **Clean Text Output:** Generates an organized plain text layout (`file1.txt`) optimized for clear reading and downstream qualitative text analysis.

---

## ⚙️ Setup & Execution

### 1. Prerequisites
Ensure you have Python 3.x installed on your computer.

### 2. Prepare Inputs
Place your raw, unorganized files containing the multi-language chapters inside the asset folder:
```bash
da_lang/assets/
```

### 3. Run the Script
Execute the main script from your terminal to process the files and generate the structured text:
```bash
python chapters.py
```

### 4. View Results
Once executed, check your root directory for the beautifully structured output file:
```bash
file1.txt
```
