############## Banking Application ####################
import os
import json
import random
from Type_conv_module import input_type1 as IT1
class User:
    branch_code= "NULL"
    balance = 0
    def __init__(self,username,acc_number=None):
        self.Name = username
        self.Account_No = acc_number
    
    # Functions signing in
    def Verify_User(self):
        return os.path.isfile(f"UserInfo-{self.Name}{(self.Account_No)%1000}.txt")

    def getAccInfo(self):
        print(f"Welcome, {self.Name}!")
        while True:    
            action = IT1(input("Select an action:\n1: Check Balance\n2: Withdraw\n3: Deposit\n4:Transfer\n"))
            with open(f"UserInfo-{self.Name}{((self.Account_No)%1000)}.txt") as file:
                    User_Info=json.load(file)
            if(not isinstance(action,str)and action in range(1,5)):
                    match action:
                        # check balance    
                        case 1: 
                            print(f"Your current balance is: {User_Info['Balance']} Rs.")
                        
                        # withdraw money
                        case 2: 
                            Withdraw_amt= IT1(input("Enter amount to withdraw: "))
                            if(not isinstance(Withdraw_amt,str)):
                                # updating balance after withdrawal
                                if(Withdraw_amt<=User_Info['Balance']):
                                    print(User_Info['Balance'])
                                    User_Info['Balance']= User_Info['Balance']-Withdraw_amt
                                    print(User_Info['Balance'])
                                    print(f"Withdrawal of Rs.{Withdraw_amt} was successful!")
                                    print(f"Current balance: {User_Info['Balance']}")
                                    with open(f"UserInfo-{self.Name}{(self.Account_No)%1000}.txt","w") as file:
                                        json.dump(User_Info,file)
                                # condition for insufficient balance
                                else:
                                    print("Insufficient Balance")
                            else:
                                print("Invalid input! Please enter numeric value only.")
                        case 3:
                            deposit_amt= IT1(input("Enter amount to deposit: "))
                            if(not isinstance(deposit_amt,str)):
                                # updating balance after credit
                                User_Info['Balance']= User_Info['Balance']+deposit_amt
                                print(f"Credit of Rs.{deposit_amt} was successful!")
                                print(f"Current balance: {User_Info['Balance']}")
                                with open(f"UserInfo-{self.Name}{(self.Account_No)%1000}.txt","w") as file:
                                    json.dump(User_Info,file)
                            else:
                                print("Invalid input! Please enter numeric value only.")
                        case 4:
                            transfer_amt = IT1(input("Enter amount to transfer: "))
                            if(transfer_amt<=User_Info['Balance']):
                                print("Details of account to transfer money:- ")
                                accN= IT1(input("Enter account number: "))
                                while True:
                                    try:
                                        if(not isinstance(accN,str)):
                                            break
                                        else:
                                            raise ValueError
                                    except Exception :
                                        accN= IT1(input("Enter a valid(numeric) account no: "))
                                name = input("Enter name of account holder: ")
                                reciever = User(name,accN)
                                flag = reciever.Verify_User()
                                if(flag):
                                    if(not isinstance(transfer_amt,str)):

                                        User_Info['Balance']= User_Info['Balance']-transfer_amt
                                        
                                        with open(f"UserInfo-{name}{(accN)%1000}.txt") as file:
                                            data_log= json.load(file)
                                        data_log['Balance']= data_log['Balance']+transfer_amt
                                        with open(f"UserInfo-{name}{(accN)%1000}.txt","w") as file:
                                            json.dump(data_log,file)
                                        print(f"Transfer of Rs.{transfer_amt} was successful!")
                                        print(f"Current balance: {User_Info['Balance']}")
                                        with open(f"UserInfo-{self.Name}{(self.Account_No)%1000}.txt","w") as file:
                                            json.dump(User_Info,file)
                                    else:
                                        print("Invalid input! Please enter numeric value only.")
                                else:
                                    print("Account does not exist!")
                            else:
                                print("Insufficient Balance!")
            else:
                action = IT1(input("Select a valid action:"))
            exit= IT1(input("1: Menu\nPress any key to exit.\n"))
            if(exit==1):
                continue
            else:
                break
    
    ## Functions to create Account
    def generateAccNo(self):
        ca = random.randint(0,9999)
        match self.branch_code:
            case "BRKGB917":
                AN=9170000+ (ca)
            case "SBI715":
                AN=7150000+ (ca)
            case "IBS313":
                AN=3130000+ (ca) 
        return AN
    def createAccount(self):
        Branch_List=["BRKGB917","SBI715", "IBS313"]
        try:
            username= self.Name
            if(len(username)>10):
                print("Entered name exceeded length!")
            while(len(username)>10):
                username= input("Please enter name (max. 10 characters): ")
            self.Name= username
            
            # branch for account to create in 
            while True:
                try:
                    branch_index = int(input("Select branch index [1:BRKGB917 ; 2:SBI715 ; 3:IBS313]: "))
                    if branch_index in range(1, 4):
                        self.branch_code = Branch_List[branch_index - 1]
                        break
                    print("Invalid selection. Try again.")
                except ValueError:
                    print("Enter a number between 1 and 3.")

            # taking input of balance by managing appropriate data types
            balance = IT1(input("Enter amount to deposit(>1000): "))
            while True:
                try:
                    if(not isinstance(IT1(balance),str)):
                        if (balance>1000):
                            break
                        if (balance<1000):
                            balance = IT1(input("Enter a Amount greater than 1000 : "))
                    else:
                        raise ValueError
                except ValueError:
                    balance = IT1(input("Enter a valid numeric Amount : "))
            # generating account number and updating balance of user
            self.Account_No=self.generateAccNo() 
            self.balance = balance
        except Exception as e:
                    print(e)
        
        # Create dictinary for user information and storing it in a text file using json
        UserInfo ={ "Name":self.Name,
                   "Branch Code": self.branch_code,
                   "Account Number": self.Account_No,
                   "Balance":self.balance}
        with open(f"UserInfo-{self.Name}{self.Account_No%1000}.txt","w") as file:
            json.dump(UserInfo,file)






print("Welcome to Joint Bank Services")
while True:
    n= int(input("1: Sign in\n2: Create new account \n"))
    if(n==1):
        name= input("Enter Username: ")
        acc_no= IT1(input("Enter Account No: "))
        while True:
            try:
                if(not isinstance(acc_no,str)):
                    user= User(name,acc_no)
                    acc_flag= user.Verify_User()
                    if(acc_flag):
                        user.getAccInfo()
                        break
                    else:
                        print("Account does not exist!")
                        break
                else:
                    raise ValueError
            except Exception :
                acc_no= IT1(input("Enter a valid(numeric) account no: "))
        break
    elif(n==2): 
        name= input("Enter name: ")
        user= User(name,None)
        user.createAccount()
        print(f"Congratulations,{user.Name}.\nYour account number is {user.Account_No}\nYour current balance is:{user.balance}")
        break
    else:
        print("Please select a valid option:")
