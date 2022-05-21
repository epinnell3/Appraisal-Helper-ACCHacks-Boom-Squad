import pdfplumber
import PyPDF2

from tkinter import filedialog as fd

file_name = fd.askopenfilename()





# opens pdf file and counts total page number
file = open(file_name,"rb")
readfile = PyPDF2.PdfFileReader(file)
page_count = (readfile.numPages)


with pdfplumber.open(file_name) as pdf:
    for i in range(0,page_count - 1):
        ind_page = pdf.pages[i]
        text = ind_page.extract_text()
        
        print(text)

print(text)