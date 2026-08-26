import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download('wordnet')

word = input("Enter a word: ")

# Get synsets
synsets = wordnet.synsets(word)

print("\nSynsets and Meanings:")
for syn in synsets:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())
    print()
