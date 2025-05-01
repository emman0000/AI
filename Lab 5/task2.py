import random
import math
from typing import List, Tuple

def calculate_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two coordinates"""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(route: List[Tuple[float, float]]) -> float:
    """Calculate total distance of a route"""
    return sum(calculate_distance(route[i], route[i-1]) for i in range(len(route)))

def generate_random_route(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Create a random initial route"""
    route = coords.copy()
    random.shuffle(route)
    return route

def generate_neighbors(route: List[Tuple[float, float]]) -> List[List[Tuple[float, float]]]:
    """Generate all possible neighbors by swapping any two cities"""
    neighbors = []
    for i in range(len(route)):
        for j in range(i+1, len(route)):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap two cities
            neighbors.append(neighbor)
    return neighbors

def hill_climbing_tsp(coords: List[Tuple[float, float]], max_iterations=1000) -> Tuple[List[Tuple[float, float]], float]:
    """
    Hill climbing algorithm for TSP
    
    Args:
        coords: List of (x,y) coordinates for delivery points
        max_iterations: Maximum iterations to prevent infinite loops
        
    Returns:
        Tuple of (optimized_route, total_distance)
    """
    # Generate initial random solution
    current_route = generate_random_route(coords)
    current_distance = total_distance(current_route)
    
    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_route)
        
        # Evaluate all neighbors
        best_neighbor = None
        best_neighbor_distance = float('inf')
        
        for neighbor in neighbors:
            distance = total_distance(neighbor)
            if distance < best_neighbor_distance:
                best_neighbor = neighbor
                best_neighbor_distance = distance
        
        # Check if we found a better solution
        if best_neighbor_distance >= current_distance:
            break  # Local optimum reached
        
        # Move to the better solution
        current_route = best_neighbor
        current_distance = best_neighbor_distance
    
    # Return to starting point to complete the cycle (optional)
    # current_route.append(current_route[0])
    # current_distance += calculate_distance(current_route[-1], current_route[-2])
    
    return current_route, current_distance

# Example usage
if __name__ == "__main__":
    # Sample delivery locations (x,y coordinates)
    delivery_points = [
        (0, 0),  # Depot
        (2, 4),
        (3, 1),
        (5, 2),
        (4, 5),
        (1, 3)
    ]
    
    optimized_route, total_dist = hill_climbing_tsp(delivery_points)
    
    print("Optimized Delivery Route:")
    for i, point in enumerate(optimized_route):
        print(f"{i+1}. {point}")
    print(f"\nTotal Distance: {total_dist:.2f} units")
