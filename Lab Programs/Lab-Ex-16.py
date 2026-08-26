import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Sundar Pichai is the CEO of Google. He was born in Chennai and works in California."

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
