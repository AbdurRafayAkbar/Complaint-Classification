import pandas as pd
from sentence_transformers import SentenceTransformer

# from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

df = pd.read_csv("data/complaints_100.csv")
complaints=df["Complaint"].to_list()
embeddings=model.encode(complaints,
                        convert_to_numpy=True,
                        normalize_embeddings=True)
# similarity=cosine_similarity(embeddings)

X=embeddings
y=df["Category"]

print(type(X))
print(X.shape)
print(y.head())
