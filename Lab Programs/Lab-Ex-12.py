sentence = input("Enter sentence: ")

grammar = [
    "S -> NP VP",
    "NP -> John",
    "NP -> Mary",
    "VP -> runs",
    "VP -> walks"
]

print("\nGrammar Rules:")
for rule in grammar:
    print(rule)

if sentence in ["John runs", "John walks", "Mary runs", "Mary walks"]:
    print("\nAccepted")
else:
    print("\nRejected")
