import random
from queens_problem import QueensProblem, count_conflicts
from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing


def run_comparison(num_trials=10, n=8):
    print(f"COMPARING HILL CLIMBING vs SIMULATED ANNEALING ({n}-QUEENS, {num_trials} TRIALS)")
    print(f"{'Trial':<6} | {'Hill Climbing Cost':<20} | {'Simulated Annealing Cost':<25}")

    hc_success = 0
    sa_success = 0

    for trial in range(1, num_trials + 1):
        # Generate the exact same random starting board for both algorithms
        start_board = [random.randint(0, n - 1) for _ in range(n)]
        problem = QueensProblem(start_board)

        # Run Hill Climbing
        hc_final, hc_cost = hill_climbing(problem, start_board)
        if hc_cost == 0:
            hc_success += 1

        # Run Simulated Annealing
        sa_final, sa_cost, sa_steps = simulated_annealing(problem, start_board)
        if sa_cost == 0:
            sa_success += 1

        print(f"{trial:<6} | {hc_cost:<20} | {sa_cost:<25}")

    print(f"SUMMARY RESULTS ({num_trials} Trials):")
    print(f" Hill Climbing Success Rate: {hc_success}/{num_trials} ({hc_success/num_trials*100:.0f}%)")
    print(f" Simulated Annealing Success Rate: {sa_success}/{num_trials} ({sa_success/num_trials*100:.0f}%)")

if __name__ == "__main__":
    run_comparison()