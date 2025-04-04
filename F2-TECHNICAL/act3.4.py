# Program to read and display student information from a file

# Step 1: Open the file in read mode
try:
    with open("students.txt", "r") as file:
        # Step 2: Read the contents of the file
        content = file.read()

        # Step 3: Display the student information
        print("Student Information:")
        print(content)

except FileNotFoundError:
    print("The file 'students.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


