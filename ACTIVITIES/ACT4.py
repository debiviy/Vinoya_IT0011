import pickle

# Function to calculate grade
def calculate_grade(class_standing, major_exam_grade):
    return 0.6 * class_standing + 0.4 * major_exam_grade

# Function to open a file and load student records
def open_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("File not found. Starting with an empty record list.")
        return []

# Function to save student records to a file
def save_file(filename, records):
    with open(filename, 'wb') as file:
        pickle.dump(records, file)
    print(f"File saved as {filename}")

# Function to show all student records (with ordering options)
def show_all_students(records, order_by="none"):
    if order_by == "last_name":
        records = sorted(records, key=lambda record: record[1][1])  # Sort by last name
    elif order_by == "grade":
        records = sorted(records, key=lambda record: calculate_grade(record[2], record[3]), reverse=True)  # Sort by grade

    for record in records:
        print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam Grade: {record[3]}, Final Grade: {calculate_grade(record[2], record[3]):.2f}")

# Function to show student record by ID
def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam Grade: {record[3]}, Final Grade: {calculate_grade(record[2], record[3]):.2f}")
            return
    print("Student not found.")

# Function to add a new student record
def add_record(records, student_id, first_name, last_name, class_standing, major_exam_grade):
    records.append((student_id, (first_name, last_name), class_standing, major_exam_grade))

# Function to edit an existing student record
def edit_record(records, student_id, first_name=None, last_name=None, class_standing=None, major_exam_grade=None):
    for i, record in enumerate(records):
        if record[0] == student_id:
            new_record = list(record)
            if first_name: new_record[1] = (first_name, new_record[1][1])
            if last_name: new_record[1] = (new_record[1][0], last_name)
            if class_standing is not None: new_record[2] = class_standing
            if major_exam_grade is not None: new_record[3] = major_exam_grade
            records[i] = tuple(new_record)
            print("Record updated.")
            return
    print("Student not found.")

# Function to delete a student record
def delete_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted.")
            return
    print("Student not found.")

# Main menu program
def student_management_system():
    records = []
    current_file = ""

    while True:
        print("\nStudent Record Management Menu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            records = open_file(filename)
            current_file = filename
        
        elif choice == '2':
            if current_file:
                save_file(current_file, records)
            else:
                print("No file open. Use 'Save As File' instead.")
        
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            save_file(filename, records)
            current_file = filename
        
        elif choice == '4':
            print("\nSelect an order for showing students:")
            print("1. Order by Last Name")
            print("2. Order by Grade")
            print("3. Show without ordering")
            order_choice = input("Enter your choice: ")
            if order_choice == '1':
                show_all_students(records, order_by="last_name")
            elif order_choice == '2':
                show_all_students(records, order_by="grade")
            else:
                show_all_students(records)
        
        elif choice == '5':
            student_id = int(input("Enter student ID to search: "))
            show_student_record(records, student_id)
        
        elif choice == '6':
            student_id = int(input("Enter student ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_standing = float(input("Enter class standing grade: "))
            major_exam_grade = float(input("Enter major exam grade: "))
            add_record(records, student_id, first_name, last_name, class_standing, major_exam_grade)
        
        elif choice == '7':
            student_id = int(input("Enter student ID to edit: "))
            first_name = input("Enter new first name (leave blank to keep current): ")
            last_name = input("Enter new last name (leave blank to keep current): ")
            class_standing = input("Enter new class standing grade (leave blank to keep current): ")
            major_exam_grade = input("Enter new major exam grade (leave blank to keep current): ")

            class_standing = float(class_standing) if class_standing else None
            major_exam_grade = float(major_exam_grade) if major_exam_grade else None

            edit_record(records, student_id, first_name, last_name, class_standing, major_exam_grade)
        
        elif choice == '8':
            student_id = int(input("Enter student ID to delete: "))
            delete_record(records, student_id)
        
        elif choice == '0':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
student_management_system()

