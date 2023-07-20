import string

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    text = text.translate(str.maketrans('', '', string.whitespace + string.punctuation))
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def order_dict(dict):
    # Sort dict dictionary by value
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

with open("./books/frankenstein.txt") as f:
    text = f.read()
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    print("")
    print("")
    char_counts = order_dict(char_count(text))
    for char in char_counts[:26]:
        print(f"The character '{char[0]}' was found {char[1]} times")


