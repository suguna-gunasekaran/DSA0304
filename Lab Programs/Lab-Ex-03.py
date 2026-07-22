from nltk.stem import PorterStemmer

ps = PorterStemmer()

word = input("Enter a word: ")

print("Original Word:", word)
print("Stemmed Word:", ps.stem(word))
