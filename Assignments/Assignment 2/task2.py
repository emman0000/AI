import random

# Data Tables
task_times = [5, 8, 4, 7, 6, 3, 9] 
facility_capacities = [24, 30, 28]  
cost_matrix = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13],
]

POP_SIZE = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
GENERATIONS = 50
PENALTY = 1000  # penalty for exceeding capacity

# generated randomly as per the nature of the algorithm
def generate_chromosome():
    return [random.randint(0, 2) for _ in range(len(task_times))]

#will be used against any exceeding capacity 
#Exceeding capacity will be penalized
# Fitness function to evaluate the cost of a chromosomee
def calculate_fitness(chrom):
    facility_time = [0, 0, 0]
    total_cost = 0

    for task_idx, facility in enumerate(chrom):
        time = task_times[task_idx]
        cost = cost_matrix[task_idx][facility]
        total_cost += time * cost
        facility_time[facility] += time

    for i in range(3):
        if facility_time[i] > facility_capacities[i]:
            total_cost += PENALTY * (facility_time[i] - facility_capacities[i])

    return 1 / total_cost

#Selection of parents using roulette wheel selection
# This method selects parents based on their fitness scores 
def roulette_wheel_selection(pop, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chrom, fit in zip(pop, fitnesses):
        current += fit
        if current >= pick:
            return chrom

# A simple exchange mutation function that swaps two genes in the chromosome
def one_point_crossover(p1, p2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, len(p1) - 2)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    return p1[:], p2[:]
#A random mutation function that swaps two genes in the chromosome for two more random genes
def mutate(chrom):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chrom)), 2)
        chrom[i], chrom[j] = chrom[j], chrom[i]
    return chrom

#Main Algo implented here :
population = [generate_chromosome() for _ in range(POP_SIZE)]
best_solution = None
best_cost = float('inf')

for generation in range(GENERATIONS):
    fitnesses = [calculate_fitness(chrom) for chrom in population]
    new_population = []

    while len(new_population) < POP_SIZE:
        parent1 = roulette_wheel_selection(population, fitnesses)
        parent2 = roulette_wheel_selection(population, fitnesses)
        child1, child2 = one_point_crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = new_population[:POP_SIZE]

    for chrom in population:
        facility_time = [0, 0, 0]
        cost = 0
        for i, fac in enumerate(chrom):
            cost += task_times[i] * cost_matrix[i][fac]
            facility_time[fac] += task_times[i]
        for i in range(3):
            if facility_time[i] > facility_capacities[i]:
                cost += PENALTY * (facility_time[i] - facility_capacities[i])
        if cost < best_cost:
            best_cost = cost
            best_solution = chrom[:]

#Best solution displayed 
print("Best Allocation (Task -> Facility):", best_solution)
print("Best Cost:", best_cost)

# Display facility times
facility_time = [0, 0, 0]
for idx, f in enumerate(best_solution):
    print(f"Task {idx+1} -> Facility {f+1}")
    facility_time[f] += task_times[idx]
print("Facility Times:", facility_time)
