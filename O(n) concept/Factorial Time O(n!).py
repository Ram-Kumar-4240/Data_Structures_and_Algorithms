# Factorial Time: O(n!)
# The operation time grows factorially with the input size.
# Example: Generating all permutations of a list.

from itertools import permutations

def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i+1]]
    total_distance += distances[route[-1]][route[0]]  # Return to starting city
    return total_distance

def tsp_brute_force(distances):
    cities = list(range(len(distances)))
    min_distance = float('inf')
    best_route = None
    
    for perm in permutations(cities):
        current_distance = calculate_total_distance(perm, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm
    
    return best_route, min_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, min_distance = tsp_brute_force(distances)
print("Best route:", route)
print("Minimum distance:", min_distance)

