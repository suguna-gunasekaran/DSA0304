import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')

sentence = input("Enter a sentence: ")
word = input("Enter the ambiguous word: ")

# Apply Lesk algorithm
sense = lesk(sentence.split(), word)

if sense:
    print("\nWord:", word)
    print("Best Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found.")
