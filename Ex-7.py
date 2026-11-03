
print("ONLINE SHOPPING SYSTEM")
print("----------------------")

# 1. Represent products and payment methods using sets
A = {"Laptop", "Mobile", "Tablet"}
B = {"UPI", "Card"}

print("Products:", A)
print("Payment Methods:", B)

# 2. Generate Cartesian product
cartesian_product = {(a, b) for a in A for b in B}

# 3. Display all possible combinations
print("\nProduct-Payment Combinations:")
for item in sorted(cartesian_product):
    print(item)

# 4. Calculate cardinality
print("\nCardinality of A:", len(A))
print("Cardinality of B:", len(B))
print("Cardinality of A x B:", len(cartesian_product))

# 5. Verify Cartesian product formula
if len(cartesian_product) == len(A) * len(B):
    print("\nVerification Successful!")
    print("|A x B| = |A| x |B|")
else:
    print("\nVerification Failed!")
