
# Euler Circuit Detection using Hierholzer's Algorithm

from collections import defaultdict

# Undirected graph using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

# Calculate degree of each vertex
print("Degree of Each Vertex:")

for vertex in graph:
    print(vertex, ":", len(graph[vertex]))

# Check whether all vertices have even degree
def has_euler_circuit(graph):
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:
            return False
    return True

# Hierholzer's algorithm
def find_euler_circuit(graph):
    if not has_euler_circuit(graph):
        print("Euler Circuit does not exist")
        return

    # Copy graph so original graph is unchanged
    g = {v: list(neighbors) for v, neighbors in graph.items()}

    start = next((v for v in g if g[v]), None)

    if start is None:
        print("No edges in the graph")
        return

    stack = [start]
    circuit = []

    while stack:
        vertex = stack[-1]

        if g[vertex]:
            neighbor = g[vertex].pop()

            # Remove the reverse edge
            g[neighbor].remove(vertex)

            stack.append(neighbor)
        else:
            circuit.append(stack.pop())

    circuit.reverse()

    print("Euler Circuit:", " -> ".join(circuit))


# Main program
if has_euler_circuit(graph):
    print("\nEuler Circuit Exists")
    find_euler_circuit(graph)
else:
    print("\nEuler Circuit does not exist")
