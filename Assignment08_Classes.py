# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# Fernando E Hernandez, 12/02/2019,Modified started script to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "products.txt"  # The name of the data file
lstOfProductObjects = []

# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class Product():
    def __init__(self, product_name: str, product_price: float):  # -- Attributes --
        try:
            self.__product_name = product_name
            self.__product_price = product_price
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

# ---Properties ---#
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except Exception as e:
            raise Exception("Prices must be numbers! \n\t" + e.__str__().title())

# -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #
# File Processing ------------------------------------------------------------- #

class FileProcessor():
    """Processes data to and from a file and a list of product objects:
     methods:
     save_data_to_file(file_name,list_of_product_objects):
     read_data_from_file(file_name): -> (a list of product objects)
     """
    @staticmethod
    def WriteListDataToFile(file_name: str, list_of_product_objects: list):
        # Desc - Write each row of data to the file
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def ReadListDataFromFile(file_name: str):
        # Desc - Read each row of data from the file
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        # Desc - Display a menu of choices to the user; returns (nothing)

        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        # Desc - Gets the menu choice from a user; returns (string)

        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows: list):
        # Desc - Shows the current items in the list; returns (nothing)

        print("******* The current items products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def Input_Product_Data():
        # Desc - Accepts Product Info Input; returns (product and price)
        try:
            name = str(input("Please enter the product name --> ").strip())
            price = float(input("Thanks, now enter the price --> ").strip())
            print()  # Add an extra line for looks
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
        return p


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

try:
    lstOfProductObjects = FileProcessor.ReadListDataFromFile(strFileName)

    while(True):
        IO.OutputMenuItems()  # Shows menu
        strChoice = IO.InputMenuChoice()  # Get menu option

        if (strChoice.strip() == '1'):
            IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list of objects
            continue  # to show the menu

        elif(strChoice.strip() == '2'):
            lstOfProductObjects.append(IO.Input_Product_Data())
            continue

        elif(strChoice == '3'):
            FileProcessor.WriteListDataToFile(strFileName, lstOfProductObjects)
            continue

        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')


# Main Body of Script  ---------------------------------------------------- #
