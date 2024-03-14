Simple Banking Project
This is a simple bank project demonstrating object-oriented programming concepts in Python.

Description
This project simulates a basic bank system with the following functionalities:

Creating bank accounts for customers
Depositing and withdrawing money from accounts
Checking the account balance
The project is implemented using object-oriented programming principles, with each bank account represented as an object.

Features
Display of the new customer details i.e gender, name and age
Deposit money into an account
Withdraw money from an account
Check the balance of an account

Usage
Clone the repository to your local machine:

git clone ttps://github.com/timothymwine/simple_banking_oop.git

Navigate to the project directory:

cd simple-bank-project

Run the main.py file:

python main.py

Follow the instructions displayed in the terminal to interact with the bank system.

Object-Oriented Design
The project is structured using object-oriented programming concepts:

Account class: Represents a bank account with attributes such as account number, account holder name, and balance. Includes methods for depositing, withdrawing, and checking the balance.
Bank class: Manages a collection of accounts and provides methods for creating new accounts and accessing existing ones.
Example
python
Copy code
# Create a bank object
bank = Bank()

# Create a new account
account1 = bank.create_account("John Doe")

# Deposit $100 into the account
account1.deposit(100)

# Withdraw $50 from the account
account1.withdraw(50)

# Check the balance
balance = account1.check_balance()
print(f"Account balance: ${balance}")
Save to grepper
Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

