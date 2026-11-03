
print("EMPLOYEE ELIGIBILITY VERIFICATION")
print("----------------------------------")

# Employee records: Name, Basic Training, Experience
employees = {
    "E1": (True, 3),
    "E2": (False, 4),
    "E3": (True, 1),
    "E4": (True, 5)
}

# Predicate 1: Basic training completed
def basic_training(training):
    return training == True

# Predicate 2: Minimum 2 years of experience
def minimum_experience(experience):
    return experience >= 2

print("\nEmployee\tTraining\tExperience\tEligibility")

for employee, details in employees.items():
    training, experience = details

    # Eligibility condition using logical AND
    eligible = basic_training(training) and minimum_experience(experience)

    status = "Eligible" if eligible else "Ineligible"

    print(employee, "\t\t", "Yes" if training else "No",
          "\t\t", experience, "\t\t", status)
