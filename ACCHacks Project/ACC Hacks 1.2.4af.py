# CONSTANTS
LISTREMOVALS = 9


def main():
    get_file()


def get_file():
    import pdfplumber
    import PyPDF2
    import csv

    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name,"rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)

    with pdfplumber.open(file_name) as pdf:
        for i in range(2,3):
            ind_page = pdf.pages[i]
            text = ind_page.extract_text()

        list_split = text.split('\n')
        # removes file lines that are not needed
        for index in range(LISTREMOVALS):
            list_split.pop(0)
        list_split.pop()
        list_split.pop()
        list_split.pop(1)
        list_split.pop(1)
        # prints users address
        address = list_split[0]
        print(address)
        # prints users living area square feet
        living_area = list_split[1]
        print(living_area)
        # extracts living area square foot
        string_1 = living_area[14]
        string_2 = living_area[15]
        string_3 = living_area[16]
        string_4 = living_area[17]
        # combines the numbers into one string
        user_square_foot = string_1+string_2+string_3+string_4
        user_validation = input('Is the square foot correct?(Y/N):').upper()
        if user_validation != 'Y' and user_validation != 'N':
            print('ERROR')
            user_validation = input('Is the square foot correct?(Y/N):').upper()
        if user_validation == 'N':
            user_square_foot = input('Please enter the correct living area:')
        print(user_square_foot)
        user_square_foot = float(user_square_foot)

        import csv

        sqft_list = []
        sale_list = []
        file_name = open("output.csv", "r")
        # read csv file as a list of lists
        out_file = csv.DictReader(file_name)

        for col in out_file:
            sqft_list.append(col['SQFT'])
            sale_list.append(col['Sale Price'])
        print(sqft_list)
        print(sale_list)

        # to convert lists to dictionary
        combination = {}
        for key in sqft_list:
            for value in sale_list:
                combination[key] = value
                sale_list.remove(value)
                break
        print(combination)

        # initializing range
        i, j = (user_square_foot - 50), (user_square_foot - 50)

        # using loop to iterate through all keys
        res = dict()
        for key, val in combination.items():
            if int(val) >= i and int(val) <= j:
                res[key] = val
        print(res)

    return

main()