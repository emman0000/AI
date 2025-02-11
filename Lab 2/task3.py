import emoji
from collections import deque

# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': []
}

#  Graph Representation with Weights
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# 🔍 Depth-Limited Search (DLS)
def dls(node, goal, depth, path):
    if depth == 0:
        return False
    if node == goal:
        path.append(node)
        return True
    if node not in tree:
        return False
    for child in tree[node]:
        if dls(child, goal, depth - 1, path):
            path.append(node)
            return True
    return False

# Iterative Deepening DFS (IDDFS)
def iterative_deepening(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(emoji.emojize(f"\n:🔍: Searching at Depth: {depth}"))  
        path = []
        if dls(start, goal, depth, path):
            print(emoji.emojize(f":chequered_flag: Goal Found! Path: {' -> '.join(reversed(path))} :trophy:"))
            return
    print(emoji.emojize(":x: Goal Not Found within given depth!"))

# Bidirectional Search
def bidirectional_search(start, goal):
    if start == goal:
        return [start]

    frontier_start = {start: None}  # BFS from Start
    frontier_goal = {goal: None}    # BFS from Goal

    queue_start = deque([start])
    queue_goal = deque([goal])

    while queue_start and queue_goal:
        #  Expand from start
        if queue_start:
            node = queue_start.popleft()
            for neighbor in graph.get(node, {}):
                if neighbor not in frontier_start:
                    frontier_start[neighbor] = node
                    queue_start.append(neighbor)
                if neighbor in frontier_goal:  # Meet in the middle
                    return construct_path(frontier_start, frontier_goal, neighbor)

        #  Expand from goal
        if queue_goal:
            node = queue_goal.popleft()
            for neighbor in graph.get(node, {}):
                if neighbor not in frontier_goal:
                    frontier_goal[neighbor] = node
                    queue_goal.append(neighbor)
                if neighbor in frontier_start:  # Meet in the middle
                    return construct_path(frontier_start, frontier_goal, neighbor)

    return None  # No path found

#  Helper function to construct path from two frontiers
def construct_path(frontier_start, frontier_goal, meet_point):
    path_start = []
    node = meet_point
    while node:
        path_start.append(node)
        node = frontier_start[node]

    path_goal = []
    node = frontier_goal[meet_point]
    while node:
        path_goal.append(node)
        node = frontier_goal[node]

    return path_start[::-1] + path_goal

#  DFS
start_node = 'A'
goal_node = 'I'
max_search_depth = 6
print(emoji.emojize("\n:rocket: Running Iterative Deepening DFS..."))
iterative_deepening(start_node, goal_node, max_search_depth)

# Bidirectional Search
print(emoji.emojize("\n:🔄: Running Bidirectional Search..."))
bidirectional_path = bidirectional_search(start_node, goal_node)
if bidirectional_path:
    print(emoji.emojize(f":checkered_flag: Shortest Path Found: {' -> '.join(bidirectional_path)} :trophy:"))
else:
    print(emoji.emojize(":x: No path found!"))

