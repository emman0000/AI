import random
import math
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt

# City coordinates (example with 10 cities)
CITIES = {
    0: (60, 200),
    1: (180, 200),
    2: (80, 180),
    3: (140, 180),
    4: (20, 160),
    5: (100, 160),
    6: (200, 160),
    7: (140, 140),
    8: (40, 120),
    9: (100, 120),
}

def calculate_distance(city1: int, city2: int) -> float:
    """Calculate Euclidean distance between two cities"""
    x1, y1 = CITIES[city1]
    x2, y2 = CITIES[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def route_distance(route: List[int]) -> float:
    """Calculate total distance of a route"""
    total = 0.0
    for i in range(len(route)):
        total += calculate_distance(route[i], route[(i+1)%len(route)])
    return total

def generate_individual() -> List[int]:
    """Generate a random individual (route)"""
    individual = list(CITIES.keys())
    random.shuffle(individual)
    return individual

def initialize_population(pop_size: int) -> List[List[int]]:
    """Create initial population"""
    return [generate_individual() for _ in range(pop_size)]

def fitness(individual: List[int]) -> float:
    """Fitness is inverse of route distance"""
    return 1 / route_distance(individual)

def selection(population: List[List[int]], fitnesses: List[float]) -> List[List[int]]:
    """Select parents using roulette wheel selection"""
    total_fitness = sum(fitnesses)
    probabilities = [f/total_fitness for f in fitnesses]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def ordered_crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    """Ordered crossover (OX) for TSP"""
    size = len(parent1)
    child = [-1] * size
    
    # Select random start/end positions
    start, end = sorted(random.sample(range(size), 2))
    
    # Copy segment from parent1
    child[start:end] = parent1[start:end]
    
    # Fill remaining with parent2's cities (in order, skipping duplicates)
    ptr = end
    for city in parent2[end:] + parent2[:end]:
        if city not in child[start:end]:
            if ptr >= size:
                ptr = 0
            child[ptr] = city
            ptr += 1
    
    return child

def swap_mutation(individual: List[int], mutation_rate: float = 0.01) -> List[int]:
    """Randomly swap two cities with probability mutation_rate"""
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm_tsp(
    generations: int = 100,
    pop_size: int = 100,
    mutation_rate: float = 0.01,
    elitism: int = 2
) -> Tuple[List[int], float]:
    """Genetic algorithm for TSP"""
    
    # Initialize population
    population = initialize_population(pop_size)
    best_individual = None
    best_distance = float('inf')
    history = []
    
    for gen in range(generations):
        # Evaluate fitness
        fitnesses = [fitness(ind) for ind in population]
        
        # Find best individual
        current_best_idx = fitnesses.index(max(fitnesses))
        current_best = population[current_best_idx]
        current_dist = route_distance(current_best)
        
        if current_dist < best_distance:
            best_individual = current_best.copy()
            best_distance = current_dist
        
        history.append(best_distance)
        
        # Create next generation
        new_population = []
        
        # Elitism: keep best individuals
        sorted_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)]
        new_population.extend(sorted_pop[:elitism])
        
        # Generate offspring
        while len(new_population) < pop_size:
            # Selection
            parents = selection(population, fitnesses)
            
            # Crossover
            child = ordered_crossover(parents[0], parents[1])
            
            # Mutation
            child = swap_mutation(child, mutation_rate)
            
            new_population.append(child)
        
        population = new_population
    
    return best_individual, best_distance, history

# Visualization functions
def plot_route(route: List[int], title: str = "Best Route"):
    """Plot the route through cities"""
    x = [CITIES[city][0] for city in route + [route[0]]]
    y = [CITIES[city][1] for city in route + [route[0]]]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o-')
    plt.title(f"{title} (Distance: {route_distance(route):.2f})")
    
    # Annotate cities
    for city, (xi, yi) in CITIES.items():
        plt.annotate(str(city), (xi, yi))
    
    plt.show()

def plot_convergence(history: List[float]):
    """Plot the convergence of the algorithm"""
    plt.figure(figsize=(10, 6))
    plt.plot(history, 'b-')
    plt.title("Convergence History")
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    best_route, best_dist, history = genetic_algorithm_tsp(
        generations=200,
        pop_size=100,
        mutation_rate=0.02,
        elitism=2
    )
    
    print("Best Route Found:")
    print(" → ".join(map(str, best_route + [best_route[0]])))
    print(f"Total Distance: {best_dist:.2f}")
    
    plot_route(best_route)
    plot_convergence(history)
