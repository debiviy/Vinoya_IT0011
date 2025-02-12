# For user to input a date in mm/dd/yyyy format
date_input = input("Enter the date (mm/dd/yyyy): ")

# Split the date input into month, day, and year
month, day, year = map(int, date_input.split('/'))

# Create a list of month names for conversion
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Format the date into a human-readable format
formatted_date = f"{months[month-1]} {day}, {year}"

# Print the formatted date
print("Date: ", formatted_date)

