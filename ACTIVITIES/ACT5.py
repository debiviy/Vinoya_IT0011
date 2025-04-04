# Function for Division
def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 / num2

# Function for Exponentiation
def exponentiate(base, exponent):
    return base ** exponent

# Function for Remainder
def remainder(num1, num2):
    if num2 == 0:
        print("Error: Remainder by zero is not allowed.")
        return None
    return num1 % num2

# Function for Summation
def summation(start, end):
    if end <= start:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

# Function to display the menu and get the user's choice
def display_menu():
    print("\nMenu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (D, E, R, F, Q): ").strip().upper()

        if choice == 'Q':
            print("Exiting the program.")
            break
        elif choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = float(input("Enter the first number: "))
                if choice != 'E':  # Exponentiation requires only one number
                    num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            if choice == 'D':
                result = divide(num1, num2)
                if result is not None:
                    print(f"The result of {num1} / {num2} is: {result}")
            elif choice == 'E':
                result = exponentiate(num1, num2)
                print(f"The result of {num1} raised to the power of {num2} is: {result}")
            elif choice == 'R':
                result = remainder(num1, num2)
                if result is not None:
                    print(f"The remainder of {num1} % {num2} is: {result}")
            elif choice == 'F':
                result = summation(int(num1), int(num2))
                if result is not None:
                    print(f"The summation from {int(num1)} to {int(num2)} is: {result}")
        else:
            print("Invalid choice. Please select a valid operation (D, E, R, F, Q).")

# Run the program
if __name__ == "__main__":
    main()
