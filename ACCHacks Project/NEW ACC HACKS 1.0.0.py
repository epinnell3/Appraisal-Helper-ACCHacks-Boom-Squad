
from tkinter import filedialog as fd

import pdfplumber
import PyPDF2

file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name,"rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)


list_pages = []
with pdfplumber.open(file_name) as pdf:
    for i in range(0, 12):
        ind_page = pdf.pages[i]
        text = ind_page.extract_text()
        list_pages.append(text)

        tables


