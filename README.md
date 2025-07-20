# 🏦 Banking System

# 📋 Overview

This project is a console-based banking system implemented in Python using MySQL as the backend database. The system allows users to manage bank accounts, perform transactions, and retrieve customer and transaction data using a menu-driven interface.
It demonstrates how to:
- Connect Python with MySQL.
- Perform Create, Read, Update, and Delete (CRUD) operations.
- Maintain database integrity through foreign keys and transaction tracking.

# 🎯 System Features
The system includes the following features:

1. ✅ Account Opening (Option 1)
- Prompts the user to enter a new account number.
- Checks whether the account number already exists.
- If not, creates a new user with:
1. Initial balance: $0.00.
2. Default status: Active.
3. Stores the user's first and last name.

2. ❌ Account Closure (Option 2)
- Prompts for an account number.
- Validates if the account exists:
1. If the account has a non-zero balance, it cannot be closed.
2. If the account is already closed, notifies the user.
3. If the account is active and has a zero balance, updates its status to Closed.

3. 💸 Withdraw Money (Option 3)
- Prompts for account number.
- Validates:
1. Account existence.
2. Account is not closed.
3. Sufficient balance for withdrawal.
4. If valid, subtracts the amount from the balance and logs the transaction in the transactions table.

4. 💰 Deposit Money (Option 4)
- Prompts for account number.
- Validates:
1. Account existence.
2. Account is not closed.
3. If valid, adds the deposit amount to the balance and logs the transaction in the transactions table.

5. 🔍 Account Inquiry (Option 5)
- Displays the account’s:
1. Customer name.
2. Account status (Active or Closed).
3. Current balance.

6. 📄 View Transactions (Option 6)
- Prompts for account number.
- If found, displays a list of all transactions (Withdrawals and Deposits) associated with that account, ordered by date.

7. 🏆 Top 5 Accounts (Option 7)
- Retrieves and displays the top five users by balance.
- If fewer than five accounts exist, all are displayed.

8. 🚪 Exit Program (Option 0)
- Terminates the program.

# 🧩 Database Schema
- The system uses MySQL and includes two main tables:
1. users.
2. transactions.

# 🛠️ Setup Instructions
- ✅ Prerequisites
1. Python 3.x.
2. MySQL Server.
3. MySQL Connector (pip install mysql-connector-python).

# ⚙️ Configuration
- Update your MySQL credentials in DataBase.py:

config = {
    "user": "your_mysql_username",
    "password": "your_mysql_password",
    "host": "localhost",
    "database": "bankDB"
}

# ▶️ How to Run
1. Ensure MySQL server is running.
2. Run the main.py script.
3. Follow the on-screen menu to perform operations.

# 📌 Notes
1. Account numbers must be unique.
2. Closed accounts cannot perform transactions.
3. The database ensures consistency through foreign keys and transaction logging.
4. The program is menu-driven and robust against invalid inputs.

# ✍️ Author
Developed by Ayham Alqanni to simulate a basic banking management system with persistent data storage and operations logic.