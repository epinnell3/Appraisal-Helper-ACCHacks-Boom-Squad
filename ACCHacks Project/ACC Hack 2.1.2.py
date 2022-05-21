# project takes input of tax appraisals from Travis County and returns the average home value based on
# similar home sizes
# Alfonso R , Erick P

# CONSTANTS
LISTREMOVALS = 9

# main function that calls get_file function
def main():
    get_file()

# get_file function imports PDF from Travis County Appraisal Office and returns average similar home value
def get_file():
    # imports modules
    import pdfplumber # used to pull all text from PDF
    import PyPDF2 # used to count total number of pages of PDF
    import tabula # used to pull table data from text pulled from PDF
    import csv # used to work with the created CSV file

    # makes a GUI
    from tkinter import filedialog as fd
    # ask user to find the PDF to be used
    file_name = fd.askopenfilename()

    # opens pdf file and counts total page number
    file = open(file_name, "rb")
    # holds all PDF pages then counts total number
    readfile = PyPDF2.PdfFileReader(file)
    page_count = (readfile.numPages)

    # empty lists to hold all PDF Pages
    list_pages = []
    list_lower_string = []

    # opens PDF of inputted file and extracts all text from each page then appends to list
    with pdfplumber.open(file_name) as pdf:
        for i in range(0, page_count - 1):
            ind_page = pdf.pages[i] # temporary variable that holds each page
            text = ind_page.extract_text() # extracts the text from the ind_page variable
            lower_text = text.lower() # sets all text to lower case to compare against specific string values
            list_pages.append(text) # appends each page to list_pages list
            list_lower_string.append(lower_text) # appends lower case text to list_lower_string list

        # pulls data from page 2 to find the users home address and home size to check against similar homes
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
        # ensures user only inputs y or n to verify that the square footage found on PDF is correct
        if user_validation != 'Y' and user_validation != 'N':
            print('ERROR')
            user_validation = input('Is the square foot correct?(Y/N):').upper()
        if user_validation == 'N':
            user_square_foot = input('Please enter the correct living area:')
        user_square_foot = float(user_square_foot)

    # empty list to holds index values
    index_list = []

    # iterates through the lower case string list and searches for specific phrases to find starting and ending
    # place of table of data needed
    for i in list_lower_string[:]:

        if "sales for market area" in i:  # finds index value of starting string to find range of data for CSV
            loc_index_1 = list_lower_string.index(i) + 1
            index_list.append(loc_index_1)  # appends index value to list

        elif "sales ratio statistics" in i:  # finds index value of end string to find range of data for CSV
            loc_index_2 = list_lower_string.index(i) + 1
            index_list.append(loc_index_2)  # appends index value to list
    # page variable used to set range of data to be converted into CSV file
    page = str(index_list[0]) + '-' + str(index_list[1])
    # creates table from pages with market area data
    tabula.read_pdf(file_name, stream=True, pages='all')
    # converts table into CSV file with only the data about similiar homes, with argument of variable pages
    tabula.convert_into(file_name, "output.csv", output_format="csv", pages=page)

    # empty lists to append CSV file data to
    sqft_str_list = []
    sqft_list = []
    sale_list = []
    sale_str_list = []

    # opens output CSV file created from PDF table data
    file_name = open("output.csv", "r")
    # read csv file as a list of lists
    out_file = csv.DictReader(file_name)

    # iterates through the SQFT and Sale Price columns of the CSV file and appends the data to respective lists
    for col in out_file:
        sqft_str_list.append(col['SQFT'])
        sale_str_list.append(col['Sale Price'])

    # list of strings to prevent errors when changing string data to float data
    title_list = ["PID", "Situs", "Address", "SQFT", "Class", "Condition", "Market Area", "Sale Date",
                  "Sale Price", "Ratio"]

    # loop to change data from columns of CSV to floats
    for val in sqft_str_list:
        if val in title_list: # checks if any of the tile list strings are in the list of data
            ind_val = 0 # if they are then nothing happens
        # if they aren't then the value removes commas and changes to a float then appends to new list
        else:
            ind_val = val.replace(",", "")
            ind_val = float(ind_val)
            sqft_list.append(ind_val)

    # check if title list string is one of the values
    for val in sale_str_list:
        if val in title_list:
            ind_val = 0
        # if tile list strings aren't then removes $ and commas then appeands to new list
        else:
            ind_val_1 = val.replace(",", "")
            ind_val_2 = ind_val_1.replace("$", "")
            ind_val = float(ind_val_2)
            sale_list.append(ind_val)

    # variables used to set minimum and maximum values of square footage
    min = user_square_foot - 50
    max = user_square_foot + 50
    # empty lists to hold all homes within min max range data
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
    # sorts from min to max sale value
    final_sale.sort()

    avg_calc = 0
    # adds the first 4 sorted values together then averages them
    for i in range(0, 4):
        avg_calc += final_sale[i]

    final_average = avg_calc / 4
    # returns the median home value price to screen
    print('This is the median home value calculated based upon your inputs:','$'+str(final_average))

    return


main()
