# Program to count vowels, consonants, spaces, and other characters

input_string = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
spaces_count = 0
others_count = 0

for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    elif char == " ":
        spaces_count += 1
    else:
        others_count += 1

print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print(f"Spaces: {spaces_count}")
print(f"Other characters: {others_count}")
