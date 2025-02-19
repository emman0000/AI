#BFS Function

tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : [],
    'F' : ['I'],
    'G' : [],
    'H' : [],
    'I' : []
}

def bfs (tree, start , goal):
    visited = [] #nodes that will be visited are stored here 
    queue = [] #queue initialised to store nodes that are to be visited
    
    visited.append(start)
    queue.append(start)
    
    while queue:
        node = queue.pop(0) #if the queue is not empty, the first element is popped out
        print(node, end = " ") 
        
        if node == goal:
            print("Goal Found")
            break
        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
start_node = 'A'
goal_node = 'I'
bfs(tree, start_node, goal_node) #calling the function with the tree, start node and goal node as arguments
