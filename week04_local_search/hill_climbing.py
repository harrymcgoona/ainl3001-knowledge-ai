"""
Week 4 — Local Search: Hill Climbing Algorithm
AINL3001 — Knowledge-Driven AI
"""

import random
from queens_problem import QueensProblem, count_conflicts

def generate_neighbours(problem, state):
    """
    Task 2: Generate all valid neighbouring states.
    
    A neighbour is a new state reached by applying a valid action 
    (moving one queen to a different row in her column).
    """
    neighbours = []
    for action in problem.actions(state):
        neighbour_state = problem.result(state, action)
        neighbours.append(neighbour_state)
    return neighbours


def hill_climbing(problem, initial_state):
    """
    Task 3: Hill Climbing algorithm (Greedy Local Search).
    
    At each step, it evaluates all neighbours and moves to the neighbour 
    with the lowest conflict cost. It stops when no neighbour offers 
    a lower cost than the current state (local minimum or plateau).
    """
    current = initial_state
    current_cost = count_conflicts(current)
    steps = 0

    print(f"Starting Board: {current} | Initial Conflicts: {current_cost}")

    while True:
        neighbours = generate_neighbours(problem, current)
        
        if not neighbours:
            break

        # Find the neighbour with the lowest conflict count
        best_neighbour = min(neighbours, key=count_conflicts)
        best_cost = count_conflicts(best_neighbour)

        # Stop if no neighbour strictly improves the cost (best_cost >= current_cost)
        if best_cost >= current_cost:
            print(f"Stopped at step {steps} (Local Minimum / Peak reached)")
            break

        # Move to the better neighbour
        current = best_neighbour
        current_cost = best_cost
        steps += 1
        print(f"  Step {steps}: Moved to {current} | Conflicts: {current_cost}")

    return current, current_cost


# EXPERIMENTATION (Task 4)
if __name__ == "__main__":
    print("RUNNING HILL CLIMBING ON 8-QUEENS")

    N = 8
    success_count = 0
    num_trials = 5

    for trial in range(1, num_trials + 1):
        print(f"\n--- TRIAL {trial} ---")
        
        # Generate a random 8-queens board
        random_board = [random.randint(0, N - 1) for _ in range(N)]
        problem = QueensProblem(random_board)
        
        final_state, final_cost = hill_climbing(problem, random_board)
        
        print(f"Final State: {final_state} | Final Conflicts: {final_cost}")
        if final_cost == 0:
            print("Status: SUCCESS (Global Optimum Found!)")
            success_count += 1
        else:
            print("Status: STUCK (Local Minimum)")

    print("\n")
    print(f"SUMMARY: Solved {success_count}/{num_trials} trials successfully.")