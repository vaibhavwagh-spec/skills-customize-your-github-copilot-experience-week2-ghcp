# Starter code for Python Text Processing assignment

# Sample input file: 'input.txt'

import string

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return ""

def process_text(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator).lower()
    words = cleaned.split()
    lines = cleaned.split('\n')
    return cleaned, len(words), len(lines)

# Add more functions for writing output and advanced features

if __name__ == "__main__":
    text = read_file('input.txt')
    cleaned, word_count, line_count = process_text(text)
    print(f"Words: {word_count}, Lines: {line_count}")
    print(cleaned)
