

def main():
    get_file()






def get_file():
    import pdfplumber
    import PyPDF2
    import tabula

    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name, "rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = readfile.numPages

    print(page_count)

    list_pages = []
    with pdfplumber.open(file_name) as pdf:
        for i in range(0, page_count - 1):
            ind_page = pdf.pages[i]
            text = ind_page.extract_text()
            list_pages.append(text)

            table_similar = pdf.pages[i].extract_table()

            #if table_similar != None:
            #    pd.DataFrame(table_similar[1::], columns=table_similar[0])

         #   print(table_similar)





    i = 0

    tables = tabula.read_pdf(file_name, stream=True, pages="all")

    tabula.convert_into(file_name, "output.csv", output_format="csv", pages="all")


    return




main()

