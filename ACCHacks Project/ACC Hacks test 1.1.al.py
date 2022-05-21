# CONSTANTS
LISTREMOVALS = 9


def main():
    get_file()


def get_file():
    import pdfplumber
    import PyPDF2

    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name,"rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)

    print(page_count)

    with pdfplumber.open(file_name) as pdf:
        for i in range(2,3):
            ind_page = pdf.pages[i]
            text = ind_page.extract_text()
            print(text)

        list_split = text.split('\n')
        print(list_split)

        for index in range(LISTREMOVALS):
            list_split.pop(0)
        list_split.pop()
        list_split.pop()
        list_split.pop(1)
        list_split.pop(1)
        print(list_split)

        address = list_split[0]
        print(address)

        living_area = list_split[1]
        print(living_area)

        land_area = list_split[2]
        print(land_area)


    #print(text)
    return

def find_market_sales ():
    market_list_string = ["market area", "sales for area", "for market area"]

    
main()