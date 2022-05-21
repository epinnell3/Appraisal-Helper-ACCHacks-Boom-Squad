def main():
    get_file()


def get_file():
    global loc_index_1, loc_index_2
    import pdfplumber
    import PyPDF2
    import tabula

    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name,"rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)

    print(page_count)

    list_pages = []
    list_lower_string = []

    list_strings = ["market area", "sales for market area"]
    with pdfplumber.open(file_name) as pdf:
        for i in range(0,page_count - 1):
            ind_page = pdf.pages[i]
            text = ind_page.extract_text()

            lower_text = text.lower()

            list_pages.append(text)
            list_lower_string.append(lower_text)






    #print(list_lower_string)




    #print(list_pages)

    i = 0

    # creates dictionary of each page of document
    dic_pages = {}
    for i in range(0, page_count - 1):
        page_number = "page_{pgs}".format(pgs=i+1)
        dic_pages[page_number] = list_pages[i]



    index_list = []
    for i in list_lower_string[:]:


        if "sales for market area" in i:
            loc_index_1 = list_lower_string.index(i)

            #print(list_lower_string[loc_index_1])

            index_list.append(int(loc_index_1))



        elif "sales ratio statistics" in i:
            loc_index_2 = list_lower_string.index(i)

            #print(list_lower_string[loc_index_2])

            index_list.append(int(loc_index_2))

    print(index_list)




    # creates table from pages with market area data
    tabula.read_pdf(file_name, stream=True, pages=index_list)


    tabula.convert_into(file_name, "output.csv", output_format="csv", pages="all")
    #print(tables)

    print(list_pages)
    return
main()

