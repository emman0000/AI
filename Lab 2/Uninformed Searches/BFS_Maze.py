maze = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

# Directions for movement (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                neighbours = []
                for dx, dy in directions: 
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                        neighbours.append((nx, ny))
                graph[(i, j)] = neighbours  # Move this line outside the inner loop
    return graph  # Move this line outside the outer loop

def bfs(graph, start, goal):
    visited = []
    queue = []
    
    visited.append(start)
    queue.append(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        
        if node == goal:
            print("\nGoal Found!")
            return  # Exit the function when the goal is found
        
        for neighbour in graph.get(node, []):  # Use .get() to avoid KeyError
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Create the graph from the maze
graph = create_graph(maze)
start_node = (0, 0)
goal_node = (2, 2)

print("\nFollowing is the BFS path: ")
bfs(graph, start_node, goal_node)
