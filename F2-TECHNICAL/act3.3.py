# Function to collect student information
def collect_student_info():
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    age = input("Enter your age: ")
    contact_number = input("Enter your contact number: ")
    course = input("Enter your course: ")

    # Create a formatted string containing the student's information
    student_info = f"Last Name: {last_name}, First Name: {first_name}, Age: {age}, Contact Number: {contact_number}, Course: {course}\n"
    
    return student_info


# Function to save the student information to a file
def save_to_file(student_info):
    try:
        with open("students.txt", "a") as file:
            file.write(student_info)
        print("Student information has been saved successfully!")
    except Exception as e:
        print(f"Error: Could not save information. {e}")


def main():
    # Collect student information
    student_info = collect_student_info()

    # Save the information to the file
    save_to_file(student_info)


# Run the program
if __name__ == "__main__":
    main()
