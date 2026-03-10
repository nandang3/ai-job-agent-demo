from pdfminer.high_level import extract_text
from docx import Document

pdf_path = "../resumes/base_resume.pdf"
docx_path = "../resumes/base_resume.docx"

try:
    text = extract_text(pdf_path)
except:
    doc = Document(docx_path)
    text = "\n".join([p.text for p in doc.paragraphs])

with open("../resumes/base_resume.txt", "w") as f:
    f.write(text)

print("Resume converted successfully")
