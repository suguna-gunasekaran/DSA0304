import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)
tags = pos_tag(words)

print("\nNoun Phrases and Meanings:")

i = 0
while i < len(tags):
    phrase = []

    # Determiner + adjectives + noun
    if tags[i][1] in ['DT', 'JJ', 'NN', 'NNS']:
        while i < len(tags) and tags[i][1] in ['DT', 'JJ', 'NN', 'NNS']:
            phrase.append(tags[i][0])
            i += 1

        if any(tag in ['NN', 'NNS'] for word, tag in tags[max(0, i-len(phrase)):i]):
            print(" ".join(phrase), "-> Entity/Object")
    else:
        i += 1
