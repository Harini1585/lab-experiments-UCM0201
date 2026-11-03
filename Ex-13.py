
from collections import deque

print("HOSPITAL SHORTEST ROUTE FINDING USING BFS")
print("------------------------------------------")

# 1. Represent hospital layout using adjacency list
graph = {
    "Emergency": ["Reception", "Pharmacy"],
    "Reception": ["Emergency", "Ward", "Laboratory"],
    "Pharmacy": ["Emergency", "ICU"],
    "Ward": ["Reception", "ICU"],
    "Laboratory": ["Reception"],
    "ICU": ["Pharmacy", "Ward"]
}

# 2. Accept source and destination
source = input("Enter source location: ")
destination = input("Enter destination location: ")

# 3. Implement BFS
def bfs(graph, source, destination):

    queue = deque([[source]])
    visited = {source}
    traversal = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        traversal.append(node)

        if node == destination:
            return path, traversal

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None, traversal


# 4. Find shortest route
if source in graph and destination in graph:

    path, traversal = bfs(graph, source, destination)

    print("\nBFS Traversal Order:", traversal)

    if path:
        print("Shortest Route:", " -> ".join(path))

        # 5. Calculate corridors
        corridors = len(path) - 1
        print("Number of Corridors Traversed:", corridors)

    else:
        print("No route found.")

else:
    print("Invalid source or destination.")
