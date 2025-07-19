
# This Python script defines several functions (Create, Read, Update, Delete) for interacting with a MySQL tables. 
# It uses the cursor and database objects imported from a module called DataBase.py.

# cursor: Used to execute SQL statements.
# database: The MySQL connection object, used to commit changes.
from DataBase_File.DataBase import cursor, database
from mysql.connector import Error


# Purpose: Adds a new row to the users table.
def add_user(account_number, first_name, last_name, status, balance):
    try:
        sql = "INSERT INTO users(account_number, first_name, last_name, status, balance) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (account_number, first_name, last_name, status, balance))
        database.commit()
        #print(f"Added log {cursor.lastrowid}")
    except Error as err:
        print(f"Error adding user: {err}")
#Apply similar blocks to all functions (get_logs, get_log, etc.).


# Purpose: Fetches all users entries, ordered by newest first.
# row[1] refers to the text column (since row[0] is id).
# NOTE: It doesn't print all details, only the text.
def get_users():

    try:

        sql = ("SELECT * FROM users ORDER BY created DESC")

        cursor.execute(sql)

        result = cursor.fetchall()

        for row in result:

            return row

    except Error as err:

        print(f"Error Getting Users: {err}")


# Purpose: Retrieves a single user by ID.
# fetchone() returns a single row (as a tuple).
# NOTE: Minor issue: the loop may not be ideal; printing print(result) would be simpler and more readable.
def get_user(id):

    try:

        sql = ("SELECT * FROM users WHERE account_number = %s")

        cursor.execute(sql, (id,))

        result = cursor.fetchone()

        if result != None:

            return result[0]

    except Error as err:

        print(f"Error Getting Users: {err}")