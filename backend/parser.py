# backend/parser.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract plain text from a PDF given its raw bytes."""
    text = ""
    # Open PDF from bytes and iterate through pages
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

# DONE PARSES PDF JUST FINE