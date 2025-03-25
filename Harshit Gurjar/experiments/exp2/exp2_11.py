number = int(input("Enter a number: "))
shift_by = int(input("Enter the number of positions to shift: "))

# Perform bitwise shift operations
left_shift = number << shift_by
right_shift = number >> shift_by

print(f"Left shift of {number} by {shift_by} positions is: {left_shift}")
print(f"Right shift of {number} by {shift_by} positions is: {right_shift}")
