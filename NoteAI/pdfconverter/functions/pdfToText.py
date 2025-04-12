import os
import argparse
from pathlib import Path

# For PDF extraction
try:
    import PyPDF2
except ImportError:
    print("PyPDF2 not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "PyPDF2"])
    import PyPDF2

# For DOC/DOCX extraction
try:
    import docx
except ImportError:
    print("python-docx not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "python-docx"])
    import docx

try:
    import textract
except ImportError:
    print("textract not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "textract"])
    import textract


def extract_from_pdf(file_path):
    """Extract text from PDF files."""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n"
        return text


def extract_from_docx(file_path):
    """Extract text from DOCX files."""
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_from_doc(file_path):
    """Extract text from DOC files using textract."""
    text = textract.process(file_path).decode('utf-8')
    return text


def extract_text(file_path, output_path=None):
    """Extract text from various document formats."""
    file_path = Path(file_path)
    
    if not file_path.exists():
        return f"Error: File {file_path} does not exist."
    
    try:
        file_extension = file_path.suffix.lower()
        
        if file_extension == '.pdf':
            text = extract_from_pdf(file_path)
        elif file_extension == '.docx':
            text = extract_from_docx(file_path)
        elif file_extension == '.doc':
            text = extract_from_doc(file_path)
        else:
            return f"Error: Unsupported file format: {file_extension}"
        
        if not text.strip():
            return f"Warning: No text extracted from {file_path}"
        
        # If output path is specified, write to file
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(text)
            return f"Text extracted successfully and saved to {output_path}"
        
        return text
    
    except Exception as e:
        return f"Error extracting text: {str(e)}"


