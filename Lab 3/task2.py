
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

    def update_edge(self, node1, node2, new_cost):
        if node1 in self.edges and node2 in self.edges[node1]:
            self.edges[node1][node2] = new_cost
            self.edges[node2][node1] = new_cost

    def get_neighbors(self, node):
        return self.edges.get(node, {})

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])  # Manhattan distance

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.edges}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.edges}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.get_neighbors(current).items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Simulating a dynamic graph with changing edge costs
def dynamic_edge_updates(graph):
    while True:
        node1, node2 = random.choice(list(graph.edges.keys())), random.choice(list(graph.edges.keys()))
        if node1 != node2 and node2 in graph.edges[node1]:
            new_cost = random.randint(1, 20)
            graph.update_edge(node1, node2, new_cost)
            print(f"Updated edge ({node1}, {node2}) with new cost: {new_cost}")
        time.sleep(random.uniform(1, 3))  # Random update interval

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
goal = (4, 4)

# Run dynamic updates in a separate thread
import threading
threading.Thread(target=dynamic_edge_updates, args=(graph,), daemon=True).start()

while True:
    path = a_star(graph, start, goal)
    print("Current Optimal Path:", path)
    time.sleep(2)  # Recompute every 2 seconds
