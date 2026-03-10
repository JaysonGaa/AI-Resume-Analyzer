# backend/analyzer.py
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a professional resume coach and ATS expert.
Given a resume and a job description, analyze how well the resume matches the job.
The job description may contain some webpage noise such as legal disclaimers, form fields, 
and navigation text — focus only on the actual job requirements and responsibilities.

Rules:
- missing_skills: skills or requirements mentioned in the JOB DESCRIPTION that are NOT present in the RESUME
- suggestions: specific changes the candidate should make to their RESUME to better match the job
- summary: 1-2 sentence overall assessment

Respond ONLY with valid JSON in this format:
{
  "missing_skills": ["skill1", "skill2", ...],
  "suggestions": ["suggestion1", "suggestion2", ...],
  "summary": "A 1-2 sentence overall assessment."
}
Do not include any explanation, markdown, or text outside the JSON."""

def analyze_with_ai(resume_text: str, job_description: str) -> dict:
    """Send resume + job description to Groq and get structured feedback."""

    prompt = f"""
RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Analyze the match and return your JSON response.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown code fences if model adds them
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)

