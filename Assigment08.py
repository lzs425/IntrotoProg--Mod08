# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# LShmait,08.29.22,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LShmait,08.29.22,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    def __init__(self, prod_name: str, prod_price: float): # constructor
        self.product_name = prod_name # attribute
        self.product_price = prod_price # attribute

    # -- Properties --
    #product_name
    @property  # "Getter" for product name
    def product_name(self):
        return str(self.__product_name_str).title()

    @product_name.setter  # "Setter" for product name
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product name can't be numeric")

    # product_cost
    @property  # "Getter" for product cost
    def product_cost(self):
        return str(self.__product_cost_flt).title()  # Title case

    @product_cost.setter  # "Setter" for product cost
    def product_cost(self, value):  #
        if (value).isnumeric() == True:
            self.__product_cost_flt = value
        else:
            raise Exception("Product cost must be numeric")

        #TODO  -- are the getters/setters necessary if I put in type in the constructor?
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

        add_new_prod_entry(lstofprod, newprodentry)- a list of product objects updated with new entry

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LShmait,08.29.22,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(fileName):
        file = open(fileName, "r")
        lines = file.readlines()
        lstofProd = {}
        ProdID = 0
        for lines in file:
            ProdID+= ProdID
            product_name, product_price = line.split(",")
            Product = Product(prod_name= product_name, prod_price=product_price)
            lstofprod[ProdID] = Product
        file.close()
        return lstofprod

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(fileName, lstofprod):
        file = open(fileName, "w")
        for row in lstofprod:
            file.write(str(row) + "\n")
        file.close()

    @staticmethod
    def add_new_prod_entry(lstofprod, newprodentry):
        lstofprod.append(newprodentry)
        return lstofprod
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Performs input and output tasks
    Methods:
        output_menu_tasks()- Displays menu to a user
        input_menu_choice()- Takes menu selection input from user, returns choice
        print_product_data()- Displays all current product names and prices
        input_new_product_info()- Takes user input for product name and price, returns new line of data
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LShmait,08.29.22,Modified code to complete assignment 8
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        print('''
        Product Data Storage
        Menu of Options

        1) View current product data
        2) Add product data to table
        3) Save the data and exit
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        choice_int = 0
        while (choice_int<1 or choice_int>3):
            try:
                choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
                choice_int = int(choice)
            except ValueError:
                print("Please only enter 1, 2, or 3")
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_product_data(lstofprod):
        print("******* Product Name and Price: *******")
        print("Product Name - Product Price")
        for row in lstofprod:
            print(str(row["ProdName"]) + " - " + str(row["ProdPrice"]))
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user

    @staticmethod
    def input_new_product_info():
        new_product_name = ""
        new_product_price = None
        while(new_product_name == "" or new_product_price is None):
            try:
                new_product_name = input("Enter the name of the product: ").strip()
                new_product_price = float(input("Enter the product price: ").strip())
                new_prod_entry = {"ProdName": new_product_name, "ProdPrice": new_product_price}
            except ValueError:
                print("Please enter a numeric value for the product cost")
        return new_prod_entry

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(fileName=strFileName)

while(True):
    # Show user a menu of options
    IO.output_menu_tasks()
    choice_str = IO.input_menu_choice() # Get user's menu option choice
    # Show user current data in the list of product objects
    if choice_str.strip() == '1': # displays current data
        IO.print_product_data(lstofprod= lstOfProductObjects)
        continue
        # Let user add data to the list of product objects
    elif choice_str.strip() == '2': # add product info to the list
        new_prod_row = IO.input_new_product_info()
        FileProcessor.add_new_prod_entry(lstofprod=lstOfProductObjects,newprodentry=new_prod_row)
        continue
        # let user save current data to file and exit program
    elif choice_str.strip() == '3':
        FileProcessor.save_data_to_file(fileName=strFileName,lstofprod=lstOfProductObjects)
        print("Data was saved! Goodbye!")
# Main Body of Script  ---------------------------------------------------- #

