
# Dijkstra's Algorithm - Shortest Path

import heapq

# Weighted graph using adjacency list
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

# Dijkstra's algorithm
def dijkstra(graph, source, destination):

    distances = {v: float('inf') for v in graph}
    previous = {v: None for v in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == destination:
            break

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(
                    priority_queue, (distance, neighbor)
                )

    # Reconstruct shortest path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if distances[destination] == float('inf'):
        print("No path exists")
    else:
        print("Shortest Path:", " -> ".join(path))
        print("Total Distance:", distances[destination])


# Main program
source = 'A'
destination = 'E'

print("Source:", source)
print("Destination:", destination)

dijkstra(graph, source, destination)
