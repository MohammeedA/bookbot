def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_num_char(words):
    characters = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    return characters