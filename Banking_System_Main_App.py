
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

        if account_number == DataBase_Functions.get_user_id(account_number):

            print("There is An Account Already in The System With That ID!")
            print("RESULT: Failed To Open An Account.")

        else:

            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")

            DataBase_Functions.add_user(account_number, first_name.capitalize(), last_name.capitalize(), "Active", 0)

            print("RESULT: Account Has Been Opened.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")


# A function that deals with deleting an account.
def close_account():

    try:

        account_number = int(input("Enter An Account Number: "))

        account_number_search = DataBase_Functions.get_user(account_number)

        if account_number_search != None:

            print(f"Customer Name: {account_number_search[1]} {account_number_search[2]}")

            if account_number_search[4] > 0:

                print("The Account Has Balance, Cannot Be Closed!")
                print("RESULT: Failed To Delete The Account.")

            elif account_number_search[3] == "Closed":

                print("The Account is Already Closed!")
                print("RESULT: Failed To Delete The Account.")

            elif account_number_search[3] == "Active" and account_number_search[4] <= 0:

                DataBase_Functions.update_user_status(account_number, "Closed")

                print("RESULT: Account Has Been Closed.")

        else:

            print("There is No Account With This Number!")
            print("RESULT: Failed To Delete The Account.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")


# A function that deals with money withdraw.
def withdraw_money():

    try:

        account_number = int(input("Enter An Account Number: "))

        account_number_search = DataBase_Functions.get_user(account_number)

        if account_number_search != None:

            print(f"Customer Name: {account_number_search[1]} {account_number_search[2]}")

            if account_number_search[3] == "Closed":

                print("The Account is Closed!")
                print("RESULT: Failed To Withdraw Money.")

            else:

                print(f"Account Balance: ${account_number_search[4]}")

                withdraw_amount = float(input("Enter The Amount To Withdraw: "))

                if withdraw_amount <= account_number_search[4]:

                    total_after_withdraw = account_number_search[4] - withdraw_amount

                    DataBase_Functions.add_transaction(account_number, "Withdraw", withdraw_amount)

                    DataBase_Functions.update_user_balance(account_number, total_after_withdraw)

                    account_number_search = DataBase_Functions.get_user(account_number)

                    print("RESULT: Transaction Completed.")

                    print(f"New Account Balance: ${account_number_search[4]}")

                else:

                    print("Insuffcient Fund!")
                    print("RESULT: Failed To Withdraw Money.")

        else:

            print("There is No Account With This Number!")
            print("RESULT: Failed To Withdraw Money.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")


# A function that deals with money deposit.
def deposit_money():

    try:

        account_number = int(input("Enter An Account Number: "))

        account_number_search = DataBase_Functions.get_user(account_number)

        if account_number_search != None:

            print(f"Customer Name: {account_number_search[1]} {account_number_search[2]}")

            if account_number_search[3] == "Closed":

                print("The Account is Closed!")
                print("RESULT: Failed To Deposit Money.")

            else:

                print(f"Account Balance: ${account_number_search[4]}")

                deposit_amount = float(input("Enter The Amount To Deposit: "))

                total_after_deposit = account_number_search[4] + deposit_amount

                DataBase_Functions.add_transaction(account_number, "Deposit", deposit_amount)

                DataBase_Functions.update_user_balance(account_number, total_after_deposit)

                account_number_search = DataBase_Functions.get_user(account_number)

                print("RESULT: Transaction Completed.")

                print(f"New Account Balance: ${account_number_search[4]}")

        else:

            print("There is No Account With This Number!")
            print("RESULT: Failed To Deposit Money.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")


# A function that deals with account inquiry.
def account_inquiry():

    try:

        account_number = int(input("Enter An Account Number: "))

        account_number_search = DataBase_Functions.get_user(account_number)

        if account_number_search != None:

            print(f"Customer Name: {account_number_search[1]} {account_number_search[2]}")

            print(f"Account Status: {account_number_search[3]}")

            print(f"Account Balance: ${account_number_search[4]}")

        else:

            print("There is No Account With This Number!")
            print("RESULT: Failed To Retrieve Account Information.")

    except ValueError:

        print("ERROR: Entered a Non Integer Value!")


# A function that deals with account transactions.
def account_transactions():

    try:

        account_number = int(input("Enter An Account Number: "))

        account_number_search = DataBase_Functions.get_user(account_number)

        if account_number_search != None:

            print(f"Customer Name: {account_number_search[1]} {account_number_search[2]}")

            print("Transactions History:")

            transactions = DataBase_Functions.get_user_transactions(account_number)

            if transactions == []:

                print("No Transactions History!")

            else:

                list_number = 1

                print(f"{"Transaction":<15}{"Transaction Type":<20}{"Amount":<10}{"Date/Time"}")

                for transaction in transactions:

                    # Extracting and formatting the datetime
                    formatted_datetime = transaction[4].strftime('%m-%d-%y %H:%M:%S')

                    print(f"{list_number}{".":<16} {transaction[2]:<16} ${transaction[3]:<9}{formatted_datetime}")

                    list_number += 1

        else:

            print("There is No Account With This Number!")
            print("RESULT: Failed To Retrieve Account Transactions.")

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

        elif user_input == 2:

            print("OPTION 2: Delete An Account")

            close_account()

            print("************************************************************")

        elif user_input == 3:

            print("OPTION 3: Withdraw Money")

            withdraw_money()

            print("************************************************************")

        elif user_input == 4:

            print("OPTION 4: Deposit Money")

            deposit_money()

            print("************************************************************")

        elif user_input == 5:

            print("OPTION 5: Account Inquiry")

            account_inquiry()

            print("************************************************************")

        elif user_input == 6:

            print("OPTION 6: Account Transactions")

            account_transactions()

            print("************************************************************")

        user_input = menu_display()

        print("************************************************************")


# Calling Main Function.
main()