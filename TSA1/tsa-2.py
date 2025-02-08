# Program to calculate the sum of digits in a given string

input_string = input("Enter a string with digits: ")
total_sum = 0

for char in input_string:
    if char.isdigit():
        total_sum += int(char)

print(f"Sum of digits: {total_sum}")
