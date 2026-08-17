from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "There is no water supply.",
    "Water is unavailable.",
    "Garbage has not been collected."
]

embeddings=model.encode(sentences)
similarity=cosine_similarity(embeddings)

print(type(embeddings))
print(embeddings.shape)
print(embeddings[:10])

print(f"Similarity => {similarity}")