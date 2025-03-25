a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swapping the numbers
a = a + b
b = a - b
a = a - b

# Output the swapped numbers
print("After swapping:")
print("First number:", a)
print("Second number:", b)