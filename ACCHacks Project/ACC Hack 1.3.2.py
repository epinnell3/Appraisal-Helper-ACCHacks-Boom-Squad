LISTREMOVALS = 9


def main():
    get_file()


def get_file():
    import pdfplumber
    import PyPDF2
    import tabula
    global file_name
    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name, "rb")
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)



    list_pages = []
    list_lower_string = []

    list_strings = ["market area", "sales for market area"]
    with pdfplumber.open(file_name) as pdf:
        for i in range(0, page_count - 1):
            ind_page = pdf.pages[i]
            text = ind_page.extract_text()

            lower_text = text.lower()

            list_pages.append(text)
            list_lower_string.append(lower_text)

    i = 0

    index_list = []
    for i in list_lower_string[:]:

        if "sales for market area" in i:  # finds index value of starting string to find range of data for CSV
            loc_index_1 = list_lower_string.index(i) + 1

            # print(list_lower_string[loc_index_1])

            index_list.append(loc_index_1)  # appends index to list


        elif "sales ratio statistics" in i:  # finds index value of end string to find range of data for CSV
            loc_index_2 = list_lower_string.index(i) + 1

            index_list.append(loc_index_2)  # appends index value to list
    # page variable used to set range of data to be converted into CSV file
    page = str(index_list[0]) + '-' + str(index_list[1])
    # creates table from pages with market area data
    tabula.read_pdf(file_name, stream=True, pages='all')
    # converts table into CSV file with only the data about similiar homes, with argument of variable pages
    tabula.convert_into(file_name, "output.csv", output_format="csv", pages=page)

    import pdfplumber

    with pdfplumber.open(file_name) as pdf:
        for i in range(2, 3):
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
        user_square_foot = string_1 + string_2 + string_3 + string_4
        user_validation = input('Is the square foot correct?(Y/N):').upper()
        if user_validation != 'Y' and user_validation != 'N':
            print('ERROR')
            user_validation = input('Is the square foot correct?(Y/N):').upper()
        if user_validation == 'N':
            user_square_foot = input('Please enter the correct living area:')
        print(user_square_foot)
        user_square_foot = float(user_square_foot)

    import csv

    sqft_str_list = []
    sale_list = []

    sqft_list = []
    sale_str_list = []

    file_name = open("output.csv", "r")
    # read csv file as a list of lists
    out_file = csv.DictReader(file_name)

    for col in out_file:
        sqft_str_list.append(col['SQFT'])
        sale_str_list.append(col['Sale Price'])

    title_list = ["PID", "Situs", "Address", "SQFT", "Class", "Condition", "Market Area", "Sale Date",
                      "Sale Price", "Ratio"]

    for val in sqft_str_list:
        if val in title_list:
            ind_val = 0

        else:
            ind_val = val.replace(",", "")
            ind_val = float(ind_val)
            sqft_list.append(ind_val)

    for val in sale_str_list:
        if val in title_list:
            ind_val = 0

        else:
            ind_val_1 = val.replace(",", "")

            ind_val_2 = ind_val_1.replace("$", "")
            ind_val = float(ind_val_2)
            sale_list.append(ind_val)

    min = user_square_foot - 50
    max = user_square_foot + 50
    # using loop to iterate through all keys

    # to convert lists to dictionary


    final_sale = []
    final_sqft = []

    for i in range(len(sqft_list)):

        if sqft_list[i] > max:
            val_1 = 0

        elif sqft_list[i] < min:
            val_1 = 0
        else:

            val_1 = sqft_list[i]
            val_2 = sale_list[i]
            final_sqft.append(val_1)
            final_sale.append(val_2)



    final_sale.sort()


    print(final_sale)
    avg_calc = 0
    for i in range(0,4):
        avg_calc += final_sale[i]


    final_average = avg_calc / 4

    print(final_average)

    return


main()
