from queue import PriorityQueue

graph = {
    'A': [('B', 5), ('C', 8)],
    'B': [('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 7)],
    'E': [('F', 2)],
    'F': [('G', 6),( 'H', 3)],
    'G': [('I', 5)],
    'H': []
}

def best_first(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))  # Heuristic search is meant for a quicker more efficient method than brute force
    # we want to find the best possible searching method
    while not pq.empty():
        cost, node = pq.get()
        if node not in visited:
            print(node, end='')
            visited.add(node)
        if node == goal:
            print("\nGoal Reached!")
            return True
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.put((weight, neighbor))
    print("\nGoal not reachable!")
    return False

# Example usage: 
print("Best-First Search Path:")
best_first(graph, 'A', 'G') #algorithm expands the nodes in order of their heuristic value

