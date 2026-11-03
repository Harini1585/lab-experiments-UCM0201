
print("STUDENT DEPARTMENT ALLOCATION")
print("--------------------------------")

# 1. Represent domain and codomain using sets
A = {1, 2, 3, 4}
B = {"IT", "CSE", "ECE"}

# 2. Represent mapping using dictionary
mapping = {
    1: "IT",
    2: "CSE",
    3: "ECE",
    4: "CSE"
}

# 3. Display the image of each student
print("Student Department Mapping:")
for student in A:
    print(student, "->", mapping[student])

# 4. Identify the range
range_set = set(mapping.values())
print("\nRange of the function:", range_set)

# 5. Check injectivity
if len(range_set) == len(A):
    print("Injective: Yes")
else:
    print("Injective: No")

# 6. Check surjectivity
if range_set == B:
    print("Surjective: Yes")
else:
    print("Surjective: No")
