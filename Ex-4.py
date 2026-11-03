
print("UNIVERSITY COURSE REGISTRATION")
print("--------------------------------")

# Set of enrolled students in each course
AI = {101, 102, 103, 104, 105}
DS = {102, 103, 106, 107}
CS = {103, 104, 108, 109}

# 1. Students enrolled in all three courses
all_three = AI & DS & CS

# 2. Students enrolled in at least one course
at_least_one = AI | DS | CS

# 3. Students enrolled only in Artificial Intelligence
only_AI = AI - (DS | CS)

# 4. Students enrolled in exactly one course
exactly_one = (AI - (DS | CS)) | (DS - (AI | CS)) | (CS - (AI | DS))

# Display results
print("AI Students:", AI)
print("Data Science Students:", DS)
print("Cybersecurity Students:", CS)

print("\nStudents enrolled in all three courses:", all_three)
print("Students enrolled in at least one course:", at_least_one)
print("Students enrolled only in AI:", only_AI)
print("Students enrolled in exactly one course:", exactly_one)
