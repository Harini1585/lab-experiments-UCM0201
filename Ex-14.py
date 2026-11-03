# Kruskal's Algorithm - Minimum Spanning Tree

# Number of substations
vertices = 5

# Weighted edges: (cost, substation1, substation2)
edges = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D'),
    (6, 'C', 'E'),
    (7, 'D', 'E')
]

# Sort edges based on cost
edges.sort()

# Initially, each vertex belongs to a separate set
parent = {}

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)

    if root1 != root2:
        parent[root2] = root1
        return True

    return False

# Initialize parent for each vertex
for v in ['A', 'B', 'C', 'D', 'E']:
    parent[v] = v

mst = []
total_cost = 0

# Kruskal's algorithm
for cost, u, v in edges:
    if union(u, v):
        mst.append((u, v, cost))
        total_cost += cost

    if len(mst) == vertices - 1:
        break

# Display Minimum Spanning Tree
print("Selected Edges in Minimum Spanning Tree:")
for u, v, cost in mst:
    print(u, "-", v, ":", cost)

print("Total Installation Cost:", total_cost)