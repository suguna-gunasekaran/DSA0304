import random

text = "natural language processing is interesting and natural language processing is useful"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigrams:
        bigrams[word] = []

    bigrams[word].append(next_word)

current = random.choice(words)
generated = [current]

for i in range(10):
    if current in bigrams:
        current = random.choice(bigrams[current])
        generated.append(current)
    else:
        break

print("Generated Text:")
print(" ".join(generated))
