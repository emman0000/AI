from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node (not used in Best-First Search)
        self.h = 0  # Heuristic value
        self.f = 0  # Final priority value

    def __lt__(self, other):
        return self.f < other.f  # Required for PriorityQueue to compare nodes

def heuristic(current_pos, end_pos):
    # Manhattan distance heuristic
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, end): #function will search from start to end in the maze 
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node = Node(end)
    
    frontier = PriorityQueue() #stores the nodes to explore next 
    frontier.put(start_node) #add the start node to start exploring
    visited = set() #saves all the visited nodes 
    
    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position
        
        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to start from the beginning
        
        visited.add(current_pos)
        
        # Generate adjacent nodes (Right, Left, Down, Up)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: #expand to adjacent nodes 
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited):
                
                new_node = Node(new_pos, current_node)
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h  # Best-First Search: f(n) = h(n)
                frontier.put(new_node)
                visited.add(new_pos)
    
    return None  # No path found

# Example maze
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

path = best_first_search(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
