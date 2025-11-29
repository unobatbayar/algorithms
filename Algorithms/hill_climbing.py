"""
Hill Climbing Algorithm

Hill Climbing is a local search optimization algorithm that starts with
an arbitrary solution and iteratively improves it by making small changes.
It stops when no better neighbor can be found.

Time Complexity: Depends on problem size and iterations
Space Complexity: O(1)

Limitations:
    - Can get stuck in local optima
    - No backtracking (greedy approach)

Variants:
    - Steepest-ascent: Chooses best neighbor
    - Random-restart: Restarts from random positions
    - Stochastic: Randomly chooses from improving neighbors
"""


import random


def hill_climbing(initial_state, cost_function, neighbor_function, max_iterations=1000):
    """
    Performs hill climbing optimization.
    
    Args:
        initial_state: Starting state
        cost_function: Function that calculates cost (lower is better)
        neighbor_function: Function that generates all neighbors
        max_iterations: Maximum number of iterations
    
    Returns:
        Best state found and its cost
    """
    current_state = initial_state
    current_cost = cost_function(current_state)
    
    for _ in range(max_iterations):
        neighbors = neighbor_function(current_state)
        
        if not neighbors:
            break
        
        # Find best neighbor
        best_neighbor = None
        best_neighbor_cost = current_cost
        
        for neighbor in neighbors:
            neighbor_cost = cost_function(neighbor)
            if neighbor_cost < best_neighbor_cost:
                best_neighbor = neighbor
                best_neighbor_cost = neighbor_cost
        
        # If no better neighbor found, we're at local optimum
        if best_neighbor_cost >= current_cost:
            break
        
        # Move to best neighbor
        current_state = best_neighbor
        current_cost = best_neighbor_cost
    
    return current_state, current_cost


def random_restart_hill_climbing(initial_state_generator, cost_function, 
                                 neighbor_function, num_restarts=10, max_iterations=1000):
    """
    Random restart hill climbing: runs hill climbing multiple times from
    random starting positions and returns the best result.
    
    Args:
        initial_state_generator: Function that generates random initial states
        cost_function: Function that calculates cost
        neighbor_function: Function that generates neighbors
        num_restarts: Number of random restarts
        max_iterations: Max iterations per restart
    
    Returns:
        Best state found across all restarts and its cost
    """
    best_state = None
    best_cost = float('infinity')
    
    for _ in range(num_restarts):
        initial = initial_state_generator()
        state, cost = hill_climbing(initial, cost_function, neighbor_function, max_iterations)
        
        if cost < best_cost:
            best_state = state
            best_cost = cost
    
    return best_state, best_cost


# Example usage
if __name__ == "__main__":
    # Simple example: minimize a function
    def simple_cost(x):
        """Cost function: (x - 5)^2"""
        return (x - 5) ** 2
    
    def simple_neighbors(x):
        """Generate neighbors by small changes."""
        step = 0.1
        return [x - step, x + step]
    
    print("Hill Climbing: Minimizing (x - 5)^2")
    initial = random.uniform(0, 10)
    best_state, best_cost = hill_climbing(initial, simple_cost, simple_neighbors)
    
    print(f"  Initial state: {initial:.4f}, cost: {simple_cost(initial):.4f}")
    print(f"  Best state: {best_state:.4f}, cost: {best_cost:.4f}")
    
    print("\nRandom Restart Hill Climbing:")
    def random_initial():
        return random.uniform(0, 10)
    
    best_state, best_cost = random_restart_hill_climbing(
        random_initial, simple_cost, simple_neighbors, num_restarts=10
    )
    print(f"  Best state: {best_state:.4f}, cost: {best_cost:.4f}")

