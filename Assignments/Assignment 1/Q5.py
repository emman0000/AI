import heapq
from collections import deque
import emoji

#map of romania with the distances between the cities
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
#heuristic values for the cities used by the search algorithms
heuristic = {"Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253, "Timisoara": 329, "Lugoj": 244, "Mehadia": 241, 
             "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193, "Pitesti": 100, "Fagaras": 176, "Bucharest": 0, "Giurgiu": 77,
             "Urziceni": 80, "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226, "Neamt": 234}

# BFS 
def bfs(start, goal):
    queue = deque([([start], 0)])  
    visited = set()

    while queue:
        path, cost = queue.popleft()
        node = path[-1]

        if node == goal:
            return path, cost 

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                new_cost = cost + edge_cost
                queue.append((path + [neighbor], new_cost))

    return None, float('inf')  

# UCS is designed to calculate the cost regardless of the path
# It will always return the shortest path
def UCS(start, goal):
    queue = [(0, [start])] 
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost  

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                new_cost = cost + edge_cost
                heapq.heappush(queue, (new_cost, path + [neighbor]))

    return None, float('inf')  

# Greedy Best First Search (GBFS)
#will use the heuristic value to determine the next node to visit
def gBFS(start, goal):
    queue = [(heuristic[start], [start], 0)]  
    visited = set()

    while queue:
        _, path, cost = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost  

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in romania.get(node, []):
                heapq.heappush(queue, (heuristic[neighbor], path + [neighbor], cost + edge_cost))

    return None, float('inf')  

# Iterative Deepening Search

def iterative(start, goal, max_depth=10):
    def dls(node, path, cost, depth):
        if node == goal:
            return path, cost  #If end of the path is reached 
        
        if depth == 0:
            return None  
        
        for neighbor, edge_cost in romania.get(node, []):
            if neighbor not in path:
                result = dls(neighbor, path + [neighbor], cost + edge_cost, depth - 1)
                if result:
                    return result  
        
        return None 

    for depth in range(max_depth): 
        result = dls(start, [start], 0, depth)
        if result:
            return result  

    return None, float('inf')  


#input from user
start = input("Enter start city: ")
goal = input("Enter goal city: ")

results = [
    ("BFS", *bfs(start, goal)),
    ("UCS", *UCS(start, goal)),
    ("GBFS", *gBFS(start, goal)),
    ("IDS", *iterative(start, goal))
]

sorted_results = sorted(results, key=lambda x: x[2])  
# Getting the best search (
best_cost = sorted_results[0][2]  
# Printing results with the best one marked
for name, path, cost in sorted_results:
    marker = "\U0001F3C6" if cost == best_cost else ""  # Add a winner trophy emoji if it's the best
    print(f"{name}: Path = {path}, Cost = {cost} {marker}")
