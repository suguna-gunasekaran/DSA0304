grammar = {
    "John runs": 0.90,
    "Mary walks": 0.85,
    "John walks": 0.70,
    "Mary runs": 0.65
}

sentence = input("Enter sentence: ")

if sentence in grammar:
    print("Sentence Accepted")
    print("Probability =", grammar[sentence])
else:
    print("Sentence Rejected")
