from stats import get_num_words, get_num_char, get_sorted_list
import sys

def get_path_to_book():
    if len(sys.argv) != 2:
        raise Exception("Usage python3 main.py <path_to_book>")
    return sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        path_to_book = get_path_to_book()
    except Exception as e:
        print(e)
    
    words = get_book_text(path_to_book)
    num_words = get_num_words(words)
    characters = get_num_char(words)
    sorted_list = get_sorted_list(characters)

    report_header = f"""""
    ============ BOOKBOT ============
    Analyzing book found at {path_to_book}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------"""
    print(report_header)
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()