
print("EQUIVALENCE RELATION ANALYSIS")
print("--------------------------------")

# 1. Represent student set
A = {1, 2, 3, 4, 5, 6}

# Academic year mapping
year = {
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 3,
    6: 3
}

print("Students:", A)
print("Academic Year Mapping:", year)

# 2. Generate relation using ordered pairs
R = set()

for a in A:
    for b in A:
        if year[a] == year[b]:
            R.add((a, b))

print("\nRelation R:")
print(sorted(R))

# 3. Check reflexivity
reflexive = all((a, a) in R for a in A)

# Check symmetry
symmetric = all((b, a) in R for (a, b) in R)

# Check transitivity
transitive = all(
    (a, c) in R
    for (a, b) in R
    for (x, c) in R if b == x
)

print("\nReflexive:", reflexive)
print("Symmetric:", symmetric)
print("Transitive:", transitive)

# 4. Check equivalence relation
if reflexive and symmetric and transitive:
    print("\nR is an EQUIVALENCE RELATION.")
else:
    print("\nR is NOT an EQUIVALENCE RELATION.")

# 5. Display equivalence classes
print("\nEquivalence Classes:")

classes = {}
for student in A:
    y = year[student]
    if y not in classes:
        classes[y] = set()
    classes[y].add(student)

for y, students in sorted(classes.items()):
    print("Year", y, ":", students)
