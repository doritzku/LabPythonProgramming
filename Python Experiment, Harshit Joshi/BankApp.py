
def create_account():
    name = input("Enter your full name: ")
    if not name:
        print("Pls fill the above field")
        exit()
    balance = float(input("Enter your bank balance: "))
    if not balance:
        print("Pls fill the above field")
        exit()
    branch = input("Enter your bank branch name: ")
    if not branch:
        print("Pls fill the above field")
        exit()
    acc_num = int(input("Enter your bank's account number: "))
    if not acc_num:
        print("Pls fill the above field")
        exit()
    return {"name": name,"balance": balance,"branch": branch,"acc_num": acc_num}

def deposit(user, amount):
    if user["branch"] != "XYZ Bank":
        raise ValueError("You do not have an account in this branch.")
    user["balance"] += amount
    return f"Deposit successful. New balance: {user['balance']}"

def withdraw(user, amount):
    if user["branch"] != "XYZ Bank":
        raise ValueError("You do not have an account in this branch.")
    if amount > user["balance"]:
        raise ValueError("The account does not have that much required balance.")
    user["balance"] -= amount
    return f"The withdrawal was successful. Balance Updated: {user['balance']}"

def login(user, account_num):
    if account_num != user["acc_num"]:
        raise ValueError("Enter the correct account number.")
    return "Login successful."

def transfer(user, amount, target_user):
    try:
        if user["balance"] < amount:
            raise ValueError("Too low balance to transfer the specified amount.")
        user["balance"] -= amount
        target_user["balance"] += amount
        return "The transfer was successful!"
    except:
        user["balance"] += amount
        return "Due to a problem in your network, the withdrawal was unsuccessful so the amount has been credited back to your account."

def main():
    print("Welcome to the XYZ Bank!")
    print("Create your account:")
    user1 = create_account()
    print("The account was created successfully!")

    while True:
        print("\nChoose an action:\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Login")
        print("4. Transfer")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount you want to deposit: "))
            try:
                print(deposit(user1, amount))
            except ValueError as x:
                print(x)

        elif choice == "2":
            amount = float(input("Enter amount you want to withdraw: "))
            try:
                print(withdraw(user1, amount))
            except ValueError as x:
                print(x)

        elif choice == "3":
            account_num = int(input("Enter your bank's account number: "))
            try:
                print(login(user1, account_num))
            except ValueError as x:
                print(x)

        elif choice == "4":
            user2_name = input("Enter the account holder's name you want to transfer money to: ")
            user2_balance = float(input("Enter the target account's current balance: "))
            user2_branch = input("Enter the target account's branch name: ")
            user2_acc_num = int(input("Enter target account number: "))
            user2 = {"name": user2_name, "balance": user2_balance, "branch": user2_branch, "acc_num": user2_acc_num}
            amount = float(input("Enter amount to transfer: "))
            try:
                if user2["name"] == user1["name"] and user2["branch"] == user1["branch"] and user2["acc_num"] == user1["acc_num"]:
                    raise ValueError("Pls enter a unique/different credentials for the transfer proccess.")
                print(transfer(user1, amount, user2))
            except ValueError as x:
                print(x)

        elif choice == "5":
            print("Thank you for using our Bank Website!")
            break

if __name__ == "__main__":
    main()