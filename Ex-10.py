
print("FIBONACCI POPULATION GROWTH")
print("----------------------------")

# 1. Accept number of generations
n = int(input("Enter the number of generations: "))

# 2. Define initial conditions
a = 0
b = 1

# 3. Generate Fibonacci sequence
sequence = []

for i in range(n):
    sequence.append(a)

    # 4. Implement recurrence relation
    c = a + b
    a = b
    b = c

# 5. Display the sequence
print("\nPopulation Sequence:")
print(sequence)

# Display population at the specified generation
if n > 0:
    print("\nPopulation at generation", n - 1, "=", sequence[n - 1])
else:
    print("\nNo generations entered.")