
from PyPDF2 import PdfFileMerger

pdfs = [pdf1_path,pdf2_path]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(pdf_res_path)
merger.close()


