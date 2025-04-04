# Step 1: Input the user's first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate the input names into a full name
full_name = first_name + " " + last_name

# Step 3: Display the full name in both upper and lower case
print("Full Name in Upper Case:", full_name.upper())
print("Full Name in Lower Case:", full_name.lower())

# Step 4: Count and display the length of the full name
name_length = len(full_name)
print("Length of Full Name:", name_length)
