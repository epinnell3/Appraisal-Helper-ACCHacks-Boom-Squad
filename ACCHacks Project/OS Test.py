
from tkinter import filedialog as fd
import tabula
import pdfplumber

file_name = fd.askopenfilename()

list_pages = []
with pdfplumber.open(file_name) as pdf:
    for i in range(0, 12):
        ind_page = pdf.pages[i]
        text = ind_page.extract_text()
        list_pages.append(text)

        tables


