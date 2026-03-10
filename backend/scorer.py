# backend/scorer.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")  # Fast & lightweight

def compute_similarity_score(resume_text: str, job_description: str) -> int:
    """Return a 0-100 match score based on semantic similarity."""
    
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    return round(float(score) * 100)


# DONE WORKS AS A GOOD SCORER