# ingestion/pdf_loader.py

import fitz  # PyMuPDF

def load_pdf(file_path: str):
    try:
        doc = fitz.open(file_path)
        return doc
    except Exception as e:
        raise Exception(f"Error loading PDF: {e}")
    
#print(fitz.__doc__)    