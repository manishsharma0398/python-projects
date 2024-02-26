from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["pdf_merger/1.pdf", "pdf_merger/dummy.pdf"]:
    merger.append(pdf)

merger.write("pdf_merger/merged-pdf.pdf")
merger.close()
