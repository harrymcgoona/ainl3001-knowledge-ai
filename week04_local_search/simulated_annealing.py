"""
Week 4 — Local Search: Simulated Annealing Algorithm
AINL3001 — Knowledge-Driven AI
"""

import math
import random
from queens_problem import QueensProblem, count_conflicts


def simulated_annealing(problem, start_board, max_steps=10000, initial_temp=100.0, cooling_rate=0.995):
    """
    Task 5: Simulated Annealing algorithm for N-Queens.
    
    Accepts worse moves probabilistically using P = exp(-delta / T)
    to escape local minima.
    """
    current = start_board.copy()
    current_cost = count_conflicts(current)
    temperature = initial_temp
    
    for step in range(1, max_steps + 1):
        # Goal reached or frozen temperature
        if current_cost == 0 or temperature <= 0.001:
            break

        # Pick a random valid action and get the neighbouring state
        actions = problem.actions(current)
        action = random.choice(actions)
        neighbour = problem.result(current, action)
        neighbour_cost = count_conflicts(neighbour)

        # Delta > 0 means neighbour is worse; Delta < 0 means neighbour is better
        delta = neighbour_cost - current_cost

        # Accept if better, OR probabilistically accept if worse
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = neighbour
            current_cost = neighbour_cost

        # Cool down temperature
        temperature *= cooling_rate

    return current, current_cost, step