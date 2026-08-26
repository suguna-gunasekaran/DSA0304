from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
documents = [
    "Python is a programming language",
    "Python is used for machine learning",
    "Machine learning is used in artificial intelligence"
]

# User query
query = input("Enter search query: ")

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + [query])

# Calculate similarity
similarity = cosine_similarity(tfidf[-1], tfidf[:-1])[0]

# Rank documents
ranking = similarity.argsort()[::-1]

print("\nDocument Ranking:")
for i in ranking:
    print("Document", i + 1, "Score:", round(similarity[i], 3))
