
# Graph Coloring - Examination Timetable Scheduling

# Subjects and their conflicts (undirected graph)
graph = {
    'Mathematics': ['Programming', 'Networks'],
    'Programming': ['Mathematics', 'Networks', 'Database'],
    'Networks': ['Mathematics', 'Programming', 'Database'],
    'Database': ['Programming', 'Networks']
}

# Greedy graph coloring algorithm
colors = {}

for subject in graph:
    used_colors = set()

    # Find colors used by adjacent subjects
    for neighbor in graph[subject]:
        if neighbor in colors:
            used_colors.add(colors[neighbor])

    # Assign the smallest available color
    color = 1
    while color in used_colors:
        color += 1

    colors[subject] = color

# Display examination timetable
print("Examination Timetable:")

for subject, color in colors.items():
    print(subject, ":", "Slot", color)

# Calculate number of colors used
total_colors = max(colors.values())

print("Total Number of Slots:", total_colors)
