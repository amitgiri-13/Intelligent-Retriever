from PyPDF2 import PdfReader
import re

def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def preprocess_text(text: str) -> str:
    text = re.sub(r"\s+"," ", text) 
    text = text.strip().lower()
    return text
