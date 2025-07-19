
from DataBase_File import DataBase_Functions
from Classes.User_Class import User


# A function that displays the menu to the user.
def menu_display():

    try:

        print("Select One From The Following:".upper())
        print("\t(1) Open An Account.")
        print("\t(2) Close An Account.")
        print("\t(3) Withdraw Money.")
        print("\t(4) Deposit Money.")
        print("\t(5) Inquiry.")
        print("\t(6) Transactions.")
        print("\t(7) Top Five Accounts.")
        print("\t(0) Exit.")

        user_input = int(input("Enter Option Selection: ".upper()))

        while user_input < 0 or user_input > 7:

            print("RESULT: Wrong Input!")

            print("************************************************************")

            print("Select One From The Following:".upper())
            print("\t(1) Open An Account.")
            print("\t(2) Close An Account.")
            print("\t(3) Withdraw Money.")
            print("\t(4) Deposit Money.")
            print("\t(5) Inquiry.")
            print("\t(6) Transactions.")
            print("\t(7) Top Five Accounts.")
            print("\t(0) Exit.")

            user_input = int(input("Enter Option Selection: ".upper()))

        return user_input
    
    except ValueError:

        print("ERROR: Entered a Non Integer Value!")

        return -1
    

# A function that deals with openning an account.
def open_account():

    try:

        account_number = int(input("Enter An Account Number: "))

        if account_number == DataBase_Functions.get_user(account_number):

            print("There is An Account Already in The System With That ID!")
            print("RESULT: Failed To Open An Account.")

        else:

            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")

            DataBase_Functions.add_user(account_number, first_name.capitalize(), last_name.capitalize(), "Active", 0)

            print("RESULT: Account Has Been Opened.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")
    

# Main Function.
def main():

    #users_dictionary = {}

    user_input = menu_display()

    print("************************************************************")

    while user_input == -1:

        user_input = menu_display()

        print("************************************************************")

    while user_input != 0:

        if user_input == 1:

            print("OPTION 1: Open An Account")

            open_account()

            print("************************************************************")

        user_input = menu_display()

        print("************************************************************")


# Calling Main Function.
main()