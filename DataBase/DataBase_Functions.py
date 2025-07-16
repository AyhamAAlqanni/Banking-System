
# This Python script defines several functions (Create, Read, Update, Delete) for interacting with a MySQL tables. 
# It uses the cursor and database objects imported from a module called DataBase.py.

# cursor: Used to execute SQL statements.
# database: The MySQL connection object, used to commit changes.
from DataBase import cursor, database


# Purpose: Adds a new row to the users table.
def add_log(text, user):

    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")      # (%s, %s) is a parameterized query to prevent SQL injection.

    cursor.execute(sql, (text, user,))

    database.commit()                           # database.commit() saves the transaction.

    log_id = cursor.lastrowid                   # cursor.lastrowid gives the ID of the inserted log.

    print("Added log {}".format(log_id))