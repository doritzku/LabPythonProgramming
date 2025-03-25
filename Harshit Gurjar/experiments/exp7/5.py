def checkDivisibility(n):
    if(n%5==0 and n%3==0):
        print("The number is divisible by both numbers")
    else:
        print("not divisible")


a=int(input("Enter a number to check divisibility: "))
checkDivisibility(a)