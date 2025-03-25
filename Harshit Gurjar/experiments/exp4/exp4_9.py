# Loop through numbers from 2 to 100
for i in range(2, 101):  
    num = "prime"  # Assume the number is prime initially

    # Loop through possible divisors from 2 to sqrt(i)
    for j in range(2, int(i ** 0.5) + 1):  
        if i % j == 0:  # If i is divisible by j, it's not prime
            num = "not prime"
            break  # Exit loop early since i is not prime

    # Print whether the number is prime or not
    print(i, "is", num)
  