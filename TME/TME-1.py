file_path = r"C:\Users\Kendra Vinoya\Downloads\numbers.txt"  

# Open the file numbers.txt
with open(file_path, 'r') as file:
    # Loop through each line in the file
    line_number = 1
    for line in file:
        # To remove any whitespace or newline characters
        line = line.strip()
        
        # Split the numbers into individual  
        numbers = line.split(',')
        
        # Sum the numbers 
        total_sum = sum(int(num) for num in numbers)
        
        # To check if the sum is a palindrome
        sum_str = str(total_sum)
        if sum_str == sum_str[::-1]:  # Palindrome check
            print(f"Line {line_number}: {line} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {line_number}: {line} (sum {total_sum}) - Not a palindrome")
        
        # To increment line number for the next line
        line_number += 1

