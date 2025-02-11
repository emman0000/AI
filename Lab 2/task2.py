from itertools import permutations

#graph made using an adjency matrix since it is easier to implement 
graph = {
    1: {2: 25, 3: 15, 4: 20},
    2: {1: 25, 3: 30, 4: 35},
    3: {1: 15, 2: 30, 4: 30},
    4: {1: 20, 2: 35, 3: 30}
}

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph [path[i]][path[i+1]]
    cost += graph [path[-1]][path[0]]
    return cost

def traveling_salesman(graph):
    cities = list(graph.keys())
    min_cost = float('inf')
    best_path = None
    
    for perm in permutations(cities):
        cost = calculate_cost(graph , perm)
        if cost<min_cost:
            min_cost = cost
            best_path = perm
    return best_path, min_cost

best_path, min_cost = traveling_salesman(graph)
print(f"Best path: {best_path}")
print(f"Minimum cost: {min_cost}")


