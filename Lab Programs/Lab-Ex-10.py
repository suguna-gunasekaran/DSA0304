sentence = input("Enter sentence: ").split()

tags = []

for word in sentence:
    tags.append("NN")

for i in range(len(sentence)):
    if sentence[i].endswith("ing"):
        tags[i] = "VBG"

    elif sentence[i].endswith("ed"):
        tags[i] = "VBD"

    elif sentence[i][0].isupper():
        tags[i] = "NNP"

print("Tagged Sentence")

for word, tag in zip(sentence, tags):
    print(word, "->", tag)
