
print("EMPLOYEE SALARY PROCESSING SYSTEM")
print("----------------------------------")

# 1. Define mathematical functions
def f(x):
    return x + 5000

def g(x):
    return 0.9 * x

# 2. Accept basic salary
salary = float(input("Enter basic salary: Rs."))

# 3. Calculate f(x)
bonus_salary = f(salary)
print("\nSalary after adding bonus:", bonus_salary)

# 4. Calculate g(f(x))
final_salary = g(f(salary))
print("Final salary after 10% tax (g(f(x))):", final_salary)

# 5. Calculate f(g(x))
other_salary = f(g(salary))
print("Salary using f(g(x)):", other_salary)

# Compare both compositions
if final_salary == other_salary:
    print("\nBoth compositions are equal.")
else:
    print("\nBoth compositions are not equal.")
    print("Function composition is NOT commutative.")
