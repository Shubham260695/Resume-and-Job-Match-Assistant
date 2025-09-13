import docx2txt
import PyPDF2

def extract_resume(file_path: str) -> str:
    """Extract text from resume (PDF/DOCX)"""
    if file_path.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file_path)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("❌ Unsupported file format (only PDF/DOCX allowed)")
    return text.strip()
