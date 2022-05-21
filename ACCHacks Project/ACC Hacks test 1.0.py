import pdfplumber
import PyPDF2

# opens pdf file and counts total page number
file = open("cad-evidence.pdf","rb")
readfile = PyPDF2.PdfFileReader(file)
page_count = (readfile.numPages)

print(page_count)

with pdfplumber.open("cad-evidence.pdf") as pdf:
    for i in range(0,page_count - 1):
        ind_page = pdf.pages[i]
        text = ind_page.extract_text()
        print(text)

print(text)