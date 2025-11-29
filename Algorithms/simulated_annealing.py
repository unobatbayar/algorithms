"""
Simulated Annealing Algorithm

Simulated Annealing is a probabilistic optimization algorithm inspired by
the annealing process in metallurgy. It's used to find approximate solutions
to optimization problems by accepting worse solutions with decreasing probability.

Time Complexity: Depends on cooling schedule and iterations
Space Complexity: O(1)

Applications:
    - Traveling Salesman Problem
    - Scheduling problems
    - Function optimization
    - Machine learning hyperparameter tuning
"""


import random
import math


def simulated_annealing(initial_state, cost_function, neighbor_function, 
                       initial_temp=1000, cooling_rate=0.95, min_temp=0.01, max_iterations=1000):
    """
    Performs simulated annealing optimization.
    
    Args:
        initial_state: Starting state
        cost_function: Function that calculates cost of a state (lower is better)
        neighbor_function: Function that generates a neighbor state
        initial_temp: Initial temperature
        cooling_rate: Rate at which temperature decreases (0 < rate < 1)
        min_temp: Minimum temperature (stopping condition)
        max_iterations: Maximum number of iterations
    
    Returns:
        Best state found and its cost
    """
    current_state = initial_state
    best_state = current_state
    best_cost = cost_function(current_state)
    current_cost = best_cost
    
    temperature = initial_temp
    iteration = 0
    
    while temperature > min_temp and iteration < max_iterations:
        # Generate neighbor
        neighbor_state = neighbor_function(current_state)
        neighbor_cost = cost_function(neighbor_state)
        
        # Calculate acceptance probability
        delta = neighbor_cost - current_cost
        
        # Accept if better, or with probability if worse
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_state = neighbor_state
            current_cost = neighbor_cost
            
            # Update best if better
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
        
        # Cool down
        temperature *= cooling_rate
        iteration += 1
    
    return best_state, best_cost


# Example: Traveling Salesman Problem (simplified)
def tsp_cost(path, distances):
    """Calculate total distance of TSP path."""
    total = 0
    for i in range(len(path)):
        total += distances[path[i]][path[(i + 1) % len(path)]]
    return total


def tsp_neighbor(path):
    """Generate neighbor by swapping two cities."""
    neighbor = path.copy()
    i, j = random.sample(range(len(neighbor)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


# Example usage
if __name__ == "__main__":
    # Simple example: minimize a function
    def simple_cost(x):
        """Cost function: (x - 5)^2"""
        return (x - 5) ** 2
    
    def simple_neighbor(x):
        """Generate neighbor by small random change."""
        return x + random.uniform(-1, 1)
    
    print("Simulated Annealing: Minimizing (x - 5)^2")
    initial = random.uniform(0, 10)
    best_state, best_cost = simulated_annealing(
        initial, simple_cost, simple_neighbor,
        initial_temp=100, cooling_rate=0.95, max_iterations=1000
    )
    
    print(f"  Initial state: {initial:.4f}, cost: {simple_cost(initial):.4f}")
    print(f"  Best state: {best_state:.4f}, cost: {best_cost:.4f}")

