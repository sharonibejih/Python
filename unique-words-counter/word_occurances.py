# Read text from a file, and count the occurence of words in that text

import string

def read_file_content(filename):
    with open(filename, "r") as f:
        texts = f.read()
    return texts


def count_words(filename):
    dict_ = {}
    text = str(read_file_content(filename))
    # remove punctuations in text
    text = text.translate(str.maketrans('', '', string.punctuation)).replace("\n","")
    # split texts into list of words
    t_list = text.strip().lower().split(" ")
    # get unique words in the list
    unique = set(t_list)
    for word in unique:
        count_ = t_list.count(word)
        count_dict = {word:count_}
        dict_.update(count_dict)
    # sort dict by values and returns the occurence of unique words in the text
    return {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1])}

# Implementation
print(count_words("./story.txt"))
