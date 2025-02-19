# BFS Function

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached!"
        return "searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached!":
            return f"Goal reached! {self.goal} found."
        else:
            return "Searching..."

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def bfs_search(self, start, goal):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")
            if node == goal:
                return f"Goal {goal} reached!"

            for neighbour in self.graph.get(node, []):  # Use self.graph instead of self.tree
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return "Goal not found!"

def run_agent(agent, environment, start_node):
    # Perform BFS search to find the goal
    search_result = environment.bfs_search(start_node, agent.goal)
    print(search_result)  # Print the result of the search

    # Get the percept (current node)
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

start_node = 'A'
goal_node = 'I'

agent = GoalBasedAgent(goal_node)
environment = Environment(tree)
run_agent(agent, environment, start_node)
