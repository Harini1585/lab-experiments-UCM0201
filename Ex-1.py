print("AUTOMATED RAILWAY SIGNALLING SYSTEM")
print("-----------------------------------")

print("P = Track Clear")
print("Q = Signal Green")
print("R = Emergency Override")

print("\nTruth Table:")
print("P\tQ\tR\tOutput")

for P in [0, 1]:
    for Q in [0, 1]:
        for R in [0, 1]:

            Output = (P and Q) or R

            print(P, "\t", Q, "\t", R, "\t", int(Output))
