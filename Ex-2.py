
print("LOGICAL EQUIVALENCE VERIFICATION")
print("--------------------------------")

print("P\tQ\tExpr1\tExpr2")

equivalent = True

for P in [0, 1]:
    for Q in [0, 1]:

        # Expression 1: NOT (P AND Q)
        expr1 = not (P and Q)

        # Expression 2: (NOT P) OR (NOT Q)
        expr2 = (not P) or (not Q)

        print(P, "\t", Q, "\t", int(expr1), "\t", int(expr2))

        if expr1 != expr2:
            equivalent = False

if equivalent:
    print("\nBoth expressions are logically equivalent.")
else:
    print("\nBoth expressions are not logically equivalent.")
