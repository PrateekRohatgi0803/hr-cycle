from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def resume_matching(model, job_description, resume_text):
    embeddings = model.encode([job_description, resume_text])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])
    score = round(similarity[0][0] * 100, 2)
    return score