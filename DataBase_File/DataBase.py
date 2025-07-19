# allows Python applications to connect to a MySQL database server and interact with it (run queries, insert data, etc.).
import mysql.connector

# This is a Python dictionary named config that contains the parameters required to connect to the MySQL database.
config = {
    "user": "bankdatabase",         # The MySQL username to log in.
    "password": "bank2025",         # The password for the user. 
    "host": "localhost",            # This specifies where the MySQL server is located. localhost means it's running on 
                                    # the same machine as the Python script.
    "database": "bankDB"            # This specifies the name of the database.
}


'''
 1. mysql.connector.connect() is a function that establishes a connection to the MySQL database.
    **config unpacks the dictionary so each key-value pair is passed as a named argument to the function 
    If the connection is successful, database now holds a connection object that lets you interact with the MySQL server.
 2. Creating a cursor object from the database connection.
    A cursor is used to execute SQL statements (like SELECT, INSERT, UPDATE, etc.) and fetch data from the database.
'''
try:
    
    database = mysql.connector.connect(**config)

    cursor = database.cursor()

    print("Connection is Successful.")

except mysql.connector.Error as err:

    print(f"Error: {err}")