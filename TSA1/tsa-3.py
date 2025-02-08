# To display pattern a
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

# To display pattern b
num = 1
row = 1
while row <= 5:
    for _ in range(row):
        print(num, end="")
    print()
    num += 2
    row += 1
