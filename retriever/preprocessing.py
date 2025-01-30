from PyPDF2 import PdfReader
import re

def read_pdf(file_path: str) -> str:
    """Read the text from pdf file.
    Args:
        file_path (str): Path of pdf file we want to read from.

    Returns:
        str:  Text contents of the pdf file.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def preprocess_text(text: str) -> str:
    """Pre process the given text string. Removes the multiple spaces, strip and convert to lowercase.
    Args:
        text (str): Raw text contents.

    Returns:
        str: Preprocessed text contents.
    """
    text = re.sub(r"\s+"," ", text) # Replace multiple spaces with single space
    text = text.strip().lower()
    return text

# Testing
if __name__ == "__main__":
    pdf_file = "/home/amit/Repositories/PythonStuffs/ArtificialIntelligence/RAGImplementation/data/corpus/raj_meera.pdf"
    text = read_pdf(pdf_file)
   
    pre_process = preprocess_text(text)
    print(pre_process)