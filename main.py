def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()