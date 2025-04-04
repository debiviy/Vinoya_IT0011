# Step 1: Concatenate first name and last name into a full name
first_name = "Davee"
last_name = "Vinoya"
full_name = first_name + " " + last_name  # Concatenation with a space in between
print("Full Name:", full_name)

# Step 2: Slice the full name to extract the first three characters of the first name
sliced_first_name = first_name[:3]
print("Sliced First Name (first 3 characters):", sliced_first_name)

# Step 3: Use string formatting to create a greeting message
greeting_message = f"Hello, {sliced_first_name}! Welcome!"
print(greeting_message)
