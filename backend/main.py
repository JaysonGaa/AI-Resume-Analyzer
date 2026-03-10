# backend/main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from parser import extract_text_from_pdf
from analyzer import analyze_with_ai
from scorer import compute_similarity_score

app = FastAPI(title="Resume Job Match Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Step 1: Extract text from uploaded PDF
    pdf_bytes = await resume.read()
    resume_text = extract_text_from_pdf(pdf_bytes)

    # Step 2: Compute semantic similarity score (0-100)
    similarity_score = compute_similarity_score(resume_text, job_description)

    # Step 3: Use AI to get detailed analysis
    ai_result = analyze_with_ai(resume_text, job_description)

    return {
        "match_score": similarity_score,
        "missing_skills": ai_result["missing_skills"],
        "suggestions": ai_result["suggestions"],
        "summary": ai_result["summary"]
    }