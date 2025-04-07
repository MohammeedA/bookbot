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

def sort_on(dict):
    return dict["count"]

def get_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        print(char)
        sorted_list.append({"char": char, "count": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list