# AI-Resume-Analyzer
A full-stack AI app that scores how well a resume matches a job description,
identifies missing skills, and suggests targeted improvements.

## Tech Stack
- **Backend**: FastAPI + Python
- **AI**: Claude API (Anthropic)
- **NLP**: sentence-transformers (semantic similarity)
- **PDF Parsing**: PyMuPDF
- **Frontend**: Streamlit

## Project Structure
```
resume-analyzer/
├── backend/
│   ├── main.py        # FastAPI app & /analyze endpoint
│   ├── parser.py      # PDF text extraction
│   ├── analyzer.py    # Claude AI integration
│   └── scorer.py      # Semantic similarity scoring
├── frontend/
│   └── app.py         # Streamlit UI
├── requirements.txt
└── README.md
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your API key
```bash
export ANTHROPIC_API_KEY=your_key_here
```

### 3. Start the backend
```bash
cd backend
uvicorn main:app --reload
```

### 4. Start the frontend
```bash
cd frontend
streamlit run app.py
```

# Screenshots
<img width="1025" height="575" alt="image" src="https://github.com/user-attachments/assets/4bd06d31-e6b9-4748-b9ed-977335a45a39" />

<img width="1138" height="927" alt="Screenshot 2026-03-18 135445" src="https://github.com/user-attachments/assets/428139be-a5ed-4e41-8ca4-7e64d6ef2e18" />
