# Given sets
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'j', 'i', 'k'}

# Elements in both A and B (Intersection of A and B)
elements_in_A_and_B = A & B
print(f"Elements in both A and B: {elements_in_A_and_B}")
print(f"Number of elements in both A and B: {len(elements_in_A_and_B)}")

# Elements in B that are not in A and C (Difference of B with A union C)
elements_in_B_not_in_A_and_C = B - (A | C)
print(f"Elements in B that are not in A and C: {elements_in_B_not_in_A_and_C}")
print(f"Number of elements in B that are not in A and C: {len(elements_in_B_not_in_A_and_C)}")

# i. Union of A, B, and C
print(f"i. {A | B | C}")

# ii. Intersection of A, B, and C
print(f"ii. {A & B & C}")

# iii. Intersection of B and C
print(f"iii. {B & C}")

# iv. Intersection of A and C
print(f"iv. {A & C}")

# v. Elements in C that are not in A or B (C - (A | B))
print(f"v. {C - (A | B)}")

# vi. Elements in B that are not in A or C (B - (A | C))
print(f"vi. {B - (A | C)}")
