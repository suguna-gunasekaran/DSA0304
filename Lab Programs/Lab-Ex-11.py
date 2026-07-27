grammar = {
    "S": [["NP", "VP"]],
    "NP": [["John"], ["Mary"]],
    "VP": [["runs"], ["walks"]]
}

def parse(symbol, words):
    if not words:
        return False

    if symbol not in grammar:
        return words[0] == symbol and len(words) == 1

    for rule in grammar[symbol]:
        if len(rule) == 2:
            for i in range(1, len(words)):
                if parse(rule[0], words[:i]) and parse(rule[1], words[i:]):
                    return True
        else:
            if parse(rule[0], words):
                return True
    return False

sentence = input("Enter sentence: ").split()

if parse("S", sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")
