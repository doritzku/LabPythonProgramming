import random
import json
import time
import os
import getpass
import hashlib
from datetime import datetime

class AccountNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class SimilarAccountError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class InvalidBankCodeError(Exception):
    pass

class InternetConnectionError(Exception):
    pass

class InvalidPinError(Exception):
    pass


class FileManager:
    def __init__(self):
        self.acc_file_path = "accounts.json"
        self.transac_file_path = "transactions.json"

    def create_acc_json(self):
        try:
            if not os.path.exists(self.acc_file_path):
                with open(self.acc_file_path, "w") as file:
                    json.dump( [], file, indent=4)
        except Exception as e:
            print(f"Error: {e}")

    def open_acc_file(self):
        if os.path.exists(self.acc_file_path):
            try:
                with open(self.acc_file_path, "r") as file:
                    accounts = json.load(file)
                    return accounts
            except json.JSONDecodeError as e:
                print(f"Error: {e}")

    def save_acc_file(self, accounts):
        with open(self.acc_file_path, "w") as file:
            json.dump(accounts, file, indent=4)

    
    def create_transaction_json(self):
        try:
            if not os.path.exists(self.transac_file_path):
                with open(self.transac_file_path, "w") as file:
                    json.dump([], file, indent=4)
        except Exception as e:
            print(f"Error: {e}")

    def open_transac_file(self):
        if os.path.exists(self.transac_file_path):
            try:
                with open(self.transac_file_path, "r") as file:
                    transactions = json.load(file)
                    return transactions
            except json.JSONDecodeError as e:
                print(f"Error: {e}")

    def save_transac_file(self, transaction):
        try:
            with open(self.transac_file_path, "r") as file:
                transactions = json.load(file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            transactions = []
        
        transactions.append(transaction)
        transactions.sort(key = lambda x: datetime.strptime(x['Timestamp'], '%Y-%m-%d %H:%M:%S'))
        
        with open(self.transac_file_path, "w") as file:
            json.dump(transactions, file, indent=4)


class AddTransaction:
    def __init__(self, file_manager):
        self.file_manager = file_manager
        
    def add_transaction(self, account_no, amount, transaction_type):
        transaction = {
            "Account Number" : account_no,
            "Amount" : amount,
            "Transaction Type" : transaction_type,
            "Timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.file_manager.save_transac_file(transaction)


class Security:
    def check_connection(self):
        return random.random() > 0.2
    
    def hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def check_pin(self, accounts, account_no):
        tries = 3
        account_manager = Account(accounts)
        account = account_manager.find_account(accounts, account_no)
        while tries != 0:
            enter_pin = getpass.getpass("Enter your PIN: ")
            if self.hash_pin(enter_pin) == account['pin']:
                return True
            else:
                print("Incorrect PIN was entered. Try again!")
                tries -= 1


class Account:
    def __init__(self, accounts=None):
        self.accounts = accounts
        
    def random_acc_no(self, accounts):
        while True:
            acc_no = random.randint(10000000000000, 99999999999999)
            acc_no = str(acc_no)
            account = self.find_account(accounts, acc_no)
            if not account:
                return acc_no
            
    def find_account(self, accounts, account_no):
        for account in accounts:
            if account['account_no'] == account_no:
                return account
            
    def create_account(self, accounts, bank_codes):
        print("\n------Create Account------")

        try:
            name = input("Enter the account holder's name: ")
            if name == "":
                raise ValueError("Account holder's name cannot be empty!")

            choice = input("Do you want to set your own account number (y/n): ")
            if choice.lower() == "y":
                account_no = input("Enter account number (must be 14 digits): ")
                if account_no == "":
                    raise ValueError("Account number cannot be empty!")
                elif len(account_no) != 14:
                    raise ValueError("Account Number must be 14 digits only!")
                elif self.find_account(accounts, account_no):
                    raise SimilarAccountError(f"Account number '{account_no}' already in use!")
            elif choice.lower() == "n":
                account_no = self.random_acc_no(accounts)
                print("------------------------------------------")
                print(f"Your account number is: {account_no}")
                time.sleep(1)
                print("Make sure to save it somewhere safe!")
                print("------------------------------------------")
                time.sleep(1)
            else:
                raise ValueError("Enter y/n only!")

            account_type = input("Account type (Savings or Current): ")
            if account_type == "":
                raise ValueError("Account type cannot be empty!")
            if account_type.lower() != "savings" and account_type.lower() != "current":
                raise ValueError("Enter a valid account type only!")

            starting_balance = input("Enter starting balance: $")
            if not starting_balance.isnumeric():
                raise ValueError("Starting Balance can only be numeric!")
            if starting_balance == "":
                raise ValueError("Starting balance cannot be empty!")
            starting_balance = float(starting_balance)
            if starting_balance < 0:
                raise InvalidAmountError("Starting balance cannot be less than zero!")

            branch_code = input("Enter the branch code (must be 6 digits): ")
            if branch_code == "":
                raise ValueError("Branch code cannot be empty!")
            if len(branch_code) != 6:
                raise ValueError("Branch Code must be 6 digits only!")

            print("\n------Available Banks------")
            for code in bank_codes:
                print(f"- {code} : {bank_codes[code]}")
            print("---------------------------")

            bank_code = input("Enter a bank code to create account: ")
            if bank_code == "":
                raise ValueError("Bank code cannot be empty!")
            if bank_code not in bank_codes:
                raise InvalidBankCodeError("Choose a given bank code!")

            print("--------------------------------")
            print("Input will not be shown!")
            time.sleep(1)
            print("Make sure to remember your PIN!")
            time.sleep(2)
            pin = getpass.getpass("Set your 4 or 6 digit PIN: ")
            if pin == "":
                raise ValueError("PIN cannot be empty!")
            if len(pin) != 4 and len(pin) != 6:
                raise ValueError("PIN should only be set as 4 or 6 digit!")
            print("--------------------------------")
            security = Security()
            hashed_pin = security.hash_pin(pin)

            ifsc_code = ""

            if bank_code == "101":
                ifsc_code = "HDFC" + "0" + branch_code
            elif bank_code == "102":
                ifsc_code = "ICIC" + "0" + branch_code
            elif bank_code == "103":
                ifsc_code = "IDFB" + "0" + branch_code

            account = {
                "name" : name,
                "account_no" : account_no,
                "account_type" : account_type,
                "balance" : starting_balance,
                "branch_code" : branch_code,
                "bank_code" : bank_code,
                "ifsc_code" : ifsc_code,
                "pin" : hashed_pin,
            }

            accounts.append(account)

            file_manager = FileManager()
            file_manager.save_acc_file(accounts)

            add_transaction = AddTransaction(file_manager)
            add_transaction.add_transaction(account_no, starting_balance, "Initial Deposit")

            print("Connecting to bank's servers...")
            time.sleep(1)
            print("Confirming account details...")
            time.sleep(1)
            print(f"Account created successfully for {account['name']}!")
            return account

        except ValueError as e:
            print(f"Error: {e}")
        except SimilarAccountError as e:
            print(f"Error: {e}")
        except InvalidAmountError as e:
            print(f"Error: {e}")
        except InvalidBankCodeError as e:
            print(f"Error: {e}")


class Banking_Operation:
    def __init__(self):
        self.file_manager = FileManager()
        self.security = Security()
        self.account_manager = Account()
        
    def deposit(self, accounts, account_no):
        try:
            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number!")

            deposit_amount = input("Enter amount to deposit: $")
            if not deposit_amount.isnumeric():
                raise ValueError("Deposit Amount can only be numeric!")
            if deposit_amount == "":
                raise ValueError("Deposit amount cannot be empty!")
            deposit_amount = float(deposit_amount)
            if deposit_amount < 0:
                raise InvalidAmountError("Deposit amount cannot be less than 0!")
            if deposit_amount > 10000000000:
                raise InvalidAmountError("You cannot deposit more than 1,000,00,00,000 in one transaction!")
            
            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return
            
            print("Connecting to bank servers...")
            time.sleep(1)
            if self.security.check_connection():
                print("Deposit was successful!")
                account['balance'] += deposit_amount
                self.file_manager.save_acc_file(accounts)
                add_transaction = AddTransaction(self.file_manager)
                add_transaction.add_transaction(account_no, deposit_amount, "Deposit")
            else:
                print("No internet connection. Try again!")

        except ValueError as e:
            print(f"Error: {e}")
        except InvalidAmountError as e:
            print(f"Error: {e}")
        except AccountNotFoundError as e:
            print(f"Error: {e}")

    def withdraw(self, accounts, account_no):
        try:
            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number!")

            withdraw_amount = input("Enter the amount you want to withdraw: $")
            if not withdraw_amount.isnumeric():
                raise ValueError("Deposit Amount can only be numeric!")
            if withdraw_amount == "":
                raise ValueError("Withdraw amount cannot be empty!")
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount < 0:
                raise InvalidAmountError("Withdraw amount cannot be less than zero!")
            if withdraw_amount > account['balance']:
                raise InsufficientFundsError("Insufficient balance!")
            if withdraw_amount > 1000000:
                raise InvalidAmountError("You cannot withdraw more than 10,00,000 in one transaction!")
            
            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return

            print("Connecting to bank servers.")
            time.sleep(1)
            if self.security.check_connection():
                print("Withdraw was successful!")
                account['balance'] -= withdraw_amount
                self.file_manager.save_acc_file(accounts)
                add_transaction = AddTransaction(self.file_manager)
                add_transaction.add_transaction(account_no, withdraw_amount, "Withdraw")
            else:   
                print("No internet connection. Try again!")

        except ValueError as e:
            print(f"Error: {e}")
        except InvalidAmountError as e:
            print(f"Error: {e}")
        except AccountNotFoundError as e:
            print(f"Error: {e}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")

    def transfer(self, accounts, account_no):
        try:
            sender_account = self.account_manager.find_account(accounts, account_no)
            if not sender_account:
                raise AccountNotFoundError("No account was found with this account number!")

            receiver_account = input("Enter the receiver's account number: ")
            receiver_account = self.account_manager.find_account(accounts, receiver_account)
            if not receiver_account:
                raise AccountNotFoundError("No account was found with this account number!")

            transfer_amount = input("Enter amount you want to transfer: $")
            if not transfer_amount.isnumeric():
                raise ValueError("Deposit Amount can only be numeric!")
            if transfer_amount == "":
                raise ValueError("Transfer amount cannot be empty!")
            transfer_amount = float(transfer_amount)
            if transfer_amount < 0:
                raise InvalidAmountError("Transfer amount cannot be less than 0!")
            if transfer_amount > sender_account['balance']:
                raise InsufficientFundsError("Insufficient balance!")
            if transfer_amount > 1000000:
                raise InvalidAmountError("You cannot transfer more than 10,00,000 in one transaction!")
            
            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return

            print("Connecting to bank servers...")
            time.sleep(1)
            if self.security.check_connection():
                print("Money was successfully transferred!")
                sender_account['balance'] -= transfer_amount
                receiver_account['balance'] += transfer_amount
                self.file_manager.save_acc_file(accounts)

                transaction = {
                "Account Number" : sender_account['account_no'],
                "Receiver Account Number" : receiver_account['account_no'],
                "Amount" : transfer_amount,
                "Transaction Type" : "Transfer",
                "Timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.file_manager.save_transac_file(transaction)
            else:
                print("No internet connection. Try again!")

        except ValueError as e:
            print(f"Error: {e}")
        except InvalidAmountError as e:
            print(f"Error: {e}")
        except AccountNotFoundError as e:
            print(f"Error: {e}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")

    def balance(self, accounts, account_no):
        try:
            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number!")

            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return

            print("Connecting to bank servers...")
            time.sleep(1)
            print("Retrieving Information...")
            time.sleep(1)
            if self.security.check_connection():
                print("\n------------BALANCE------------")
                print(f"Account No.: XX{account['account_no'][10:14]}")
                print(f"Balance: ${account['balance']}")
                print("---------------------------------")
            else:
                print("No internet connection. Try again!")

        except AccountNotFoundError as e:
            print(f"Error: {e}")

    def acc_details(self, accounts, account_no):
        try:
            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number!")

            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return

            print("\n-----------ACCOUNT DETAILS-----------")
            print(f"Account Name: {account['name']}")
            print(f"Account Number: {account['account_no']}")
            print(f"Account Type: {account['account_type'].capitalize()}")
            print(f"Account Balance: ${account['balance']}")
            print(f"IFSC Code: {account['ifsc_code']}")
            print("-------------------------------------")

        except AccountNotFoundError as e:
            print(f"Error: {e}")

    def transactions_log(self, accounts, account_no):
        try:
            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number")
            
            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return
            
            print("\n----------------Transaction Log------------------")
            transaction = self.file_manager.open_transac_file()
            transaction_found = False

            for val in transaction:
                if val['Account Number'] == account_no or val.get('Receiver Account Number') == account_no:
                    transaction_found = True
                    
                    print("\n--------------------------------------------")
                    if 'Receiver Account Number' in val:
                        print(f"Sender Account Number: {val['Account Number']}")
                        print(f"Receiver Account Number: {val['Receiver Account Number']}")
                    else:
                        print(f"Account Number: {val['Account Number']}")
                    print(f"Amount: {val['Amount']}")
                    print(f"Transaction Type: {val['Transaction Type']}")
                    print(f"Timestamp: {val['Timestamp']}")
                    print("--------------------------------------------")
                           
            if not transaction_found:
                print("No Transactions Found!")

        except AccountNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def login_acc(self, accounts):
        try:
            account_no = input("Enter your account number: ")
            if account_no == "":
                raise ValueError("Account number cannot be empty!")

            account = self.account_manager.find_account(accounts, account_no)
            if not account:
                raise AccountNotFoundError("No account was found with this account number")

            if not self.security.check_pin(accounts, account_no):
                print("Too many incorrect PIN. Returning to menu!")
                return

            return account_no

        except ValueError as e:
            print(f"Error: {e}")
        except AccountNotFoundError as e:
            print(f"Error: {e}")


class Menu:
    def __init__(self):
        self.banking_operation = Banking_Operation()
        self.file_manager = FileManager()
        
    def menu(self, accounts, account_no):
        is_running = True
        account_manager = Account()

        while is_running:
            time.sleep(1)
            print("\n===========================================")
            account = account_manager.find_account(accounts, account_no)
            bank = ""
            if account['bank_code'] == "101":
                bank = "HDFC"
            elif account['bank_code'] == "102":
                bank = "ICICI"
            elif account['bank_code'] == "103":
                bank = "IDFC"
            print(f"    Welcome to {bank} Bank Netbanking    ")
            print("===========================================")
            print(f"Hello {account['name']}, Welcome!")
            print(f"Account No.: XX{account['account_no'][10:14]}")
            print("===========================================")

            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Transfer Money")
            print("4. Check Balance")
            print("5. Show Account Details")
            print("6. Show Transactions")
            print("7. Logout")

            print("===========================================")

            pick = input("Enter your pick (1-7): ")

            if pick == "1":
                self.banking_operation.deposit(accounts, account_no)
            elif pick == "2":
                self.banking_operation.withdraw(accounts, account_no)
            elif pick == "3":
                self.banking_operation.transfer(accounts, account_no)
            elif pick == "4":
                self.banking_operation.balance(accounts, account_no)
            elif pick == "5":
                self.banking_operation.acc_details(accounts, account_no)
            elif pick == "6":
                self.banking_operation.transactions_log(accounts, account_no)
            elif pick == "7":
                self.file_manager.save_acc_file(accounts)
                is_running = False
                print("Logging out!")
                time.sleep(1)
                print(f"Thank you for using {bank} Bank Netbanking!")
            else:
                print("Please enter a pick from 1-6 only!")


class Banking_System:
    def __init__(self):
        self.file_manager = FileManager()
        self.account_manager = Account()
        self.banking_operation = Banking_Operation()
        self.menu_manager = Menu()
        
    def main(self):
        self.file_manager.create_acc_json()
        accounts = self.file_manager.open_acc_file()

        self.file_manager.create_transaction_json()
        transactions = self.file_manager.open_transac_file()

        bank_codes = {
            '101': 'HDFC Bank', 
            '102': 'ICICI Bank', 
            '103': 'IDFC Bank'
            }


        is_True = True

        while is_True:
            time.sleep(1)
            print("\n===========================================")
            print("     Welcome to Central Banking System    ")
            print("===========================================")
            print("1. Open New Account")
            print("2. Login")
            print("3. Exit")
            print("===========================================")

            option = (input("Enter your pick (1-3): "))

            if option == "1":
                self.account_manager.create_account(accounts, bank_codes)
            elif option == "2":
                account_no = self.banking_operation.login_acc(accounts)
                if account_no:
                    self.menu_manager.menu(accounts, account_no)
            elif option == "3":
                self.file_manager.save_acc_file(accounts)
                is_True = False
                print("-------------------------------------------")
                print("Thank you for using Central Banking System!")
                print("Have a good day ahead!")
                print("-------------------------------------------")
            else:
                print("Enter choice between 1-3 only!")

if __name__ == "__main__":
    banking_system = Banking_System()
    banking_system.main()