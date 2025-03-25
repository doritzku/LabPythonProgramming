class InvalidAccountNumber(Exception):
    pass
class UnidentifiedError(Exception):
    pass
class InsufficientBalance(Exception):
    pass
class invalidamount(Exception):
    pass
class IncorrectPin(Exception):
    pass
condition=0
accountNum=(input("Enter the account number: "))   #account numbers availabe are 11111,22222,33333,44444 and their pins are 1111,2222,......
with open("accounts.txt","r") as file:
    try:
            
        if f"{accountNum}.txt\n" in file.readlines():
            with open(f"{accountNum}.txt","r") as file1:
                Name=file1.readline()
                Account=int(file1.readline())
                Pin=int(file1.readline())
                Balance=float(file1.readline())
                BranchCode=file1.readline()
                condition=1
        else:
            raise InvalidAccountNumber("Account does not exist")
    except Exception as e:
        print(e)

if condition==1:
    print("Welcome to Virtual Banking Sytems")
    print(f"Hi {Name}How may i help you today?\nYou may choose the following options:")
    print("1 for Withdraw")
    print("2 for Deposit")
    print("3 to Check Balance")
    print("4 to Transfer to another account")
    print("5 to Exit\n")
    n=int(input(""))
    while(n!=5):
        if(n==1):

            withdraw_amt=int(input("How much amount would you like to withdraw sir?\n"))
            enteredpin=int(input("Enter your 4 digit pin: "))
            try:
                if enteredpin==Pin:
                    if withdraw_amt>Balance:
                        raise InsufficientBalance("Not enough balance")    
                    elif withdraw_amt<=0:
                            raise invalidamount("Enter a valid amount")
                    else:
                        print("Withdraw successfull")
                        with open(f"{accountNum}.txt","w") as file1:
                            Balance=Balance-withdraw_amt
                            file1.write(f"{Name}{Account}\n{Pin}\n{Balance}\n{BranchCode}")
                            print(f"Remaining balance is {Balance}")
                else:
                        raise IncorrectPin("Entered Pin is incorrect")
            except Exception as e:
                    print(e)
            
        if(n==2):
                deposit_amt=int(input("Enter the amout you want to deposit:\n"))
                enteredpin=int(input("Enter your 4 digit pin:\n"))
                try:
                    if enteredpin==Pin:
                        if deposit_amt<=0:
                            raise invalidamount("Invalid Amount Entered")
                        else:
                            with open(f"{accountNum}.txt","w") as file1:
                                Balance=Balance+deposit_amt
                                file1.write(f"{Name}{Account}\n{Pin}\n{Balance}\n{BranchCode}")
                        print("Deposit successfull")
                        print(f"Remaining balance is {Balance}")

                except Exception as e:
                    print(e)

        if(n==3):
            print(f"Remaining balance is: {Balance}")

        if(n==4):
            receiver_account=int(input("Enter receiver's account: "))

            with open(f"accounts.txt","r") as file:
                if f"{receiver_account}.txt\n" in file:
                    with open(f"{receiver_account}.txt","r") as file1:

                        receiver_name=file1.readline()
                        receiver_account=int(file1.readline())
                        receiver_pin=int(file1.readline())
                        receiver_balance=float(file1.readline())
                        receiver_BranchCode=file1.readline()
                        transfer_amt=int(input("Enter amount to transfer: "))

                        try:
                            if transfer_amt<=Balance:
                                with open(f"{accountNum}.txt","w") as file1:
                                    Balance=Balance-transfer_amt
                                    file1.write(f"{Name}{Account}\n{Pin}\n{Balance}\n{BranchCode}")
                                    print("Transaction successfull")
                                    print(f"Remaining balance in your account is {Balance}")
                                with open(f"{receiver_account}.txt","w") as file2:
                                    new=f'''{receiver_name}{receiver_account}
{receiver_pin}
{receiver_balance}
{receiver_BranchCode}'''
                                    file2.write(new) 
                        
                            elif transfer_amt<=0:
                                raise invalidamount("Enter a valid amount")
                    
                            else:
                                raise InsufficientBalance("Not enough balance")
                            
                        except Exception as e:
                            print(e)


        print("What you want to do now?")
        print("1 for Withdraw")
        print("2 for Deposit")
        print("3 to Check Balance")
        print("4 to Transfer to another account")
        print("5 to Exit\n")
        n=int(input(""))