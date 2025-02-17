import heapq
import random
import time

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, cost):
        if node1 not in self.edges:
            self.edges[node1] = {}
        if node2 not in self.edges:
            self.edges[node2] = {}
        self.edges[node1][node2] = cost
        self.edges[node2][node1] = cost  # Assuming undirected graph

    def get_neighbors(self, node):
        return self.edges.get(node, {})

def heuristic(node, deliveries):
    return deliveries.get(node, float('inf'))  # Prioritize stricter deadlines

def greedy_best_first_search(graph, start, deliveries):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, deliveries), start))  # Priority queue based on deadline urgency
    came_from = {}
    total_distance = 0
    visited = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        
        if current in deliveries:
            deliveries.pop(current)
            if not deliveries:
                break  # All deliveries completed
        
        for neighbor, cost in graph.get_neighbors(current).items():
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic(neighbor, deliveries), neighbor))  # Prioritize by deadline
                came_from[neighbor] = current
                total_distance += cost
    
    return total_distance, came_from

# Example usage
graph = Graph()

# Adding edges (Example: A grid-like structure)
for i in range(5):
    for j in range(5):
        if i < 4:
            graph.add_edge((i, j), (i+1, j), random.randint(1, 10))
        if j < 4:
            graph.add_edge((i, j), (i, j+1), random.randint(1, 10))

start = (0, 0)
deliveries = {
    (1, 3): 2,  # Delivery point with a deadline priority
    (3, 2): 1,
    (4, 4): 3
}

total_distance, route = greedy_best_first_search(graph, start, deliveries)
print("Total Distance Traveled:", total_distance)
print("Delivery Route:", route)

