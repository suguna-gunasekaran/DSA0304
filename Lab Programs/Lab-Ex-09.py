import re

sentence = input("Enter sentence: ")

words = sentence.split()

for word in words:

    if re.search(r'ing$', word):
        tag = "VBG"

    elif re.search(r'ed$', word):
        tag = "VBD"

    elif re.search(r'ly$', word):
        tag = "RB"

    elif re.search(r's$', word):
        tag = "NNS"

    else:
        tag = "NN"

    print(word, "->", tag)
