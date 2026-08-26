import re

text = input("Enter a sentence: ")

words = text.split()
pronouns = ["he", "she", "it", "they", "him", "her", "them"]

last_noun = None

print("\nReference Resolution:")

for word in words:
    clean = re.sub(r'[^\w]', '', word)

    if clean.lower() not in pronouns and clean[0:1].isupper():
        last_noun = clean

    if clean.lower() in pronouns and last_noun:
        print(clean, "->", last_noun)
