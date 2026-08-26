import re

text = input("Enter text: ")

sentences = re.split(r'[.!?]+', text)
sentences = [s.strip().lower() for s in sentences if s.strip()]

print("\nCoherence Analysis:")

scores = []

for i in range(len(sentences) - 1):
    words1 = set(re.findall(r'\b\w+\b', sentences[i]))
    words2 = set(re.findall(r'\b\w+\b', sentences[i + 1]))

    common = words1 & words2

    if words1 | words2:
        score = len(common) / len(words1 | words2)
    else:
        score = 0

    scores.append(score)

    print("Sentence", i + 1, "and", i + 2,
          "-> Score:", round(score, 2))

if scores:
    average = sum(scores) / len(scores)
    print("\nAverage Coherence Score:", round(average, 2))

    if average >= 0.2:
        print("Text is Coherent")
    else:
        print("Text has Low Coherence")
else:
    print("Enter at least two sentences.")
