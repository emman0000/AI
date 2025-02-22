import heapq
from collections import deque

romania = { 
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Urziceni", 85), ("Giurgiu", 90)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)]
}

heuristic = {"Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253, "Timisoara": 329, "Lugoj": 244, "Mehadia": 241, 
             "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193, "Pitesti": 100, "Fagaras": 176, "Bucharest": 0, "Giurgiu": 77,
             "Urziceni": 80, "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234}

# BFS with Path Cost Calculation
def bfs(start, goal):
    queue = deque([([start], 0)])  # (path, cost)
    visited = set()

    while queue:
        path, cost = queue.popleft()
        node = path[-1]

        if node == goal:
            return path, cost  # Return path and total cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                new_cost = cost + edge_cost
                queue.append((path + [neighbor], new_cost))

    return None, float('inf')  # No path found

# UCS (already returns cost)
def UCS(start, goal):
    queue = [(0, [start])]  # (cost, path)
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost  # Return path and total cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                new_cost = cost + edge_cost
                heapq.heappush(queue, (new_cost, path + [neighbor]))

    return None, float('inf')  # No path found

# Greedy Best First Search (GBFS) - No Cost Calculation Needed
def gBFS(start, goal):
    queue = [(heuristic[start], [start], 0)]  # (heuristic, path, cost)
    visited = set()

    while queue:
        _, path, cost = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost  # Return path and total cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                heapq.heappush(queue, (heuristic[neighbor], path + [neighbor], cost + edge_cost))

    return None, float('inf')  # No path found

# Iterative Deepening Search (IDS) with Cost Calculation
def iterative(start, goal, max_depth=10):
    def dls(node, path, cost, depth):
        if depth == 0 and node == goal:
            return path, cost  # If depth reached and goal is found

        if depth > 0:
            for neighbor, edge_cost in romania.get(node, []):
                if neighbor not in path:
                    result = dls(neighbor, path + [neighbor], cost + edge_cost, depth - 1)
                    if result:
                        return result  # Return first successful path found

        return None, float('inf')  # No path found at this depth

    for depth in range(max_depth):  # Increase depth iteratively
        result, cost = dls(start, [start], 0, depth)
        if result:
            return result, cost

    return None, float('inf')  # No path found within depth limit

# Running all algorithms and comparing costs
start, goal = "Arad", "Bucharest"

results = [
    ("BFS", *bfs(start, goal)),
    ("UCS", *UCS(start, goal)),
    ("GBFS", *gBFS(start, goal)),
    ("IDS", *iterative(start, goal))
]

# Sorting results based on path cost in ascending order
sorted_results = sorted(results, key=lambda x: x[2])  # Sort by cost (third element in tuple)

# Printing results
for name, path, cost in sorted_results:
    print(f"{name}: Path = {path}, Cost = {cost}")
