import random

tag_dictionary = {
    "dog": ["NN"],
    "runs": ["VB", "NNS"],
    "fast": ["RB", "JJ"]
}

sentence = input("Enter sentence: ").split()

print("POS Tags:")

for word in sentence:
    if word in tag_dictionary:
        tag = random.choice(tag_dictionary[word])
    else:
        tag = "NN"

    print(word, "->", tag)
