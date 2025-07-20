
from fpdf import FPDF
import uuid

def export_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.splitlines():
        pdf.multi_cell(0, 10, line)
    path = f"/mnt/data/{uuid.uuid4()}.pdf"
    pdf.output(path)
    return path
