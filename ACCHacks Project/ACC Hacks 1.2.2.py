def main():
    get_file()
    csv_reader()


def get_file():

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



    index_list = []
    for i in list_lower_string[:]:


        if "sales for market area" in i: # finds index value of starting string to find range of data for CSV
            loc_index_1 = list_lower_string.index(i) + 1

            #print(list_lower_string[loc_index_1])

            index_list.append(loc_index_1) # appends index to list


        elif "sales ratio statistics" in i: # finds index value of end string to find range of data for CSV
            loc_index_2 = list_lower_string.index(i) + 1

            index_list.append(loc_index_2) # appends index value to list
    # page variable used to set range of data to be converted into CSV file
    page = str(index_list[0])+'-'+str(index_list[1])
    # creates table from pages with market area data
    tabula.read_pdf(file_name, stream=True, pages='all')
    # converts table into CSV file with only the data about similiar homes, with argument of variable pages
    tabula.convert_into(file_name, "output.csv", output_format="csv", pages=page)



    return


def csv_reader():

    # importing the module
    import pandas as pd

    data = pd.read_csv('output.csv')
    # you can also use df['column_name']
        # converting column data to list
    square_feet = data['SQFT'].tolist()
    sale_price = data['Sale Price'].tolist()
    print(square_feet)
    print(sale_price)

    return

main()

