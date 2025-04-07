from stats import get_num_words, get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(words)
    characters = get_num_char(words)
    print(f"{num_words} words found in the document")
    print(characters)

main()