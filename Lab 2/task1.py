import heapq

# Define the graph with costs (for UCS)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3), ('G', 6)],
    'D': [('H', 7)],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

goal_node = 'E'


# Goal-Based Agent for DFS
class DFSAgent:
    def __init__(self, goal):
        self.goal = goal

    def dfs_search(self, environment, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")

            if node == self.goal:
                return f"Goal {self.goal} found!"

            if node not in visited:
                visited.add(node)
                for neighbor, _ in reversed(environment.get_neighbors(node)):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return "Goal not found"


# Goal-Based Agent for Depth-Limited Search (DLS)
class DLSAgent:
    def __init__(self, goal, limit):
        self.goal = goal
        self.limit = limit

    def dls_search(self, environment, start, depth=0):
        if start == self.goal:
            return f"Goal {self.goal} found!"

        if depth >= self.limit:
            return "Depth limit reached, goal not found"

        print(f"Visiting: {start}, Depth: {depth}")
        for neighbor, _ in environment.get_neighbors(start):
            result = self.dls_search(environment, neighbor, depth + 1)
            if "found" in result:
                return result

        return "Goal not found"


# Utility-Based Agent for Uniform Cost Search (UCS)
class UCSAgent:
    def __init__(self, goal):
        self.goal = goal

    def ucs_search(self, environment, start):
        priority_queue = [(0, start)]  # (cost, node)
        visited = {}

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)
            print(f"Visiting: {node}, Cost: {cost}")

            if node == self.goal:
                return f"Goal {self.goal} found with cost {cost}"

            if node not in visited or cost < visited[node]:
                visited[node] = cost
                for neighbor, step_cost in environment.get_neighbors(node):
                    new_cost = cost + step_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return "Goal not found"


# Environment
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbors(self, node):
        return self.graph.get(node, [])


# Instantiate Environment
env = Environment(graph)

# Instantiate Agents
dfs_agent = DFSAgent(goal_node)
dls_agent = DLSAgent(goal_node, limit=2)
ucs_agent = UCSAgent(goal_node)

# Run Searches
print("\nDFS Agent:")
print(dfs_agent.dfs_search(env, 'A'))

print("\nDLS Agent (limit=2):")
print(dls_agent.dls_search(env, 'A'))

print("\nUCS Agent:")
print(ucs_agent.ucs_search(env, 'A'))
