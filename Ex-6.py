
print("STUDENT PREREQUISITE RELATION ANALYSIS")
print("--------------------------------------")

# Set of courses
A = {1, 2, 3}

# Relation represented using ordered pairs
R = {
    (1, 1), (2, 2), (3, 3),
    (1, 2), (1, 3), (2, 3)
}

print("Course Set:", A)
print("Relation:", R)

# Check reflexivity
reflexive = all((a, a) in R for a in A)
print("\nReflexive:", reflexive)

# Check symmetry
symmetric = all((b, a) in R for (a, b) in R)
print("Symmetric:", symmetric)

# Check antisymmetry
antisymmetric = all(
    a == b or (b, a) not in R
    for (a, b) in R
)
print("Antisymmetric:", antisymmetric)

# Check transitivity
transitive = all(
    (a, c) in R
    for (a, b) in R
    for (x, c) in R if b == x
)
print("Transitive:", transitive)

# Check partial order
if reflexive and antisymmetric and transitive:
    print("\nThe relation is a PARTIAL ORDER.")
else:
    print("\nThe relation is NOT a PARTIAL ORDER.")
