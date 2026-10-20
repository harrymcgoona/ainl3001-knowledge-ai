"""
AINL3001 — Knowledge-Driven AI
Week 5 — Constraint Satisfaction Problems
BSP 2026

Australian map colouring: six regions and three colours.

Tasks
-----
0. Examine an invalid assignment.
1. Understand variables, domains and constraints.
2. Implement constraint checking.
3. Implement backtracking with simple variable selection.
4. Compare backtracking with brute force.
5. Improve variable selection using MRV.

Work in this starter file and commit your progress to your own fork.
"""

# --------------------------------------------------
# TASK 0 — MANUAL EXPLORATION
# --------------------------------------------------

example_assignment = {
    "WA": "Red",
    "NT": "Red",
    "SA": "Green",
    "Q": "Blue",
    "NSW": "Red",
    "V": "Green",
}

print("Manual CSP Exploration")
print(example_assignment)
print("\nQuestions:")
print("1. Is this assignment valid?")
print("This assignment is invalid.")
print("2. Which neighbouring pairs violate a constraint?")
print("WA-NT and NSW-V (along with SA-V) violate constraints because adjacent regions share the same colour.")
print("3. How could you correct the assignment?")
print("By changing conflicting region colours so no adjacent pairs share a colour.")
print("4. Why is it useful to detect violations early?")
print("It saves work by pruning invalid partial assignments before exploring entire search branches.")

# --------------------------------------------------
# TASK 1 — CSP REPRESENTATION
# --------------------------------------------------

# Each variable is an Australian region.
variables = ["WA", "NT", "SA", "Q", "NSW", "V"]

# Each region may use one of these three colours.
domains = {
    variable: ["Red", "Green", "Blue"]
    for variable in variables
}

# Each pair of neighbouring regions must have different colours.
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]

# --------------------------------------------------
# TASK 2 — CONSTRAINT CHECKING
# --------------------------------------------------

def is_valid_assignment(assignment):
    """Return True if a complete OR partial assignment is valid."""
    for var1, var2 in constraints:
            # Check if BOTH regions in a constraint pair have been assigned
            if var1 in assignment and var2 in assignment:
                # If neighbouring regions have the same colour, it's invalid
                if assignment[var1] == assignment[var2]:
                    return False
    return True


# --------------------------------------------------
# TASK 3 AND TASK 5 — VARIABLE SELECTION
# --------------------------------------------------

def select_unassigned_variable(assignment, use_mrv=True):
    """Choose the next unassigned region.

    Task 3: First return the FIRST unassigned region.

    Task 5: Replace that approach with MRV (Minimum Remaining Values):
    choose the unassigned region with the FEWEST currently legal
    colours. Break ties by keeping the first region in variables.
    """
    unassigned = [v for v in variables if v not in assignment]
    if not unassigned:
        return None

    if not use_mrv:
        # Task 3: Simple variable selection (first unassigned)
        return unassigned[0]

    # Task 5: Minimum Remaining Values (MRV) heuristic
    best_variable = None
    min_legal_count = float('inf')

    for var in unassigned:
        legal_count = 0
        for colour in domains[var]:
            # Temporarily assign colour and check validity
            assignment[var] = colour
            if is_valid_assignment(assignment):
                legal_count += 1
            # Undo temporary assignment
            del assignment[var]

        if legal_count < min_legal_count:
            min_legal_count = legal_count
            best_variable = var

    return best_variable



# --------------------------------------------------
# TASK 3 — BACKTRACKING SEARCH
# --------------------------------------------------

def backtracking_search(assignment, use_mrv=True):
    """Return a complete valid assignment, or None if none exists."""
    # 1. Base case: If all variables are assigned, return a copy of solution
    if len(assignment) == len(variables):
        return assignment.copy()

    # 2. Select an unassigned variable
    var = select_unassigned_variable(assignment, use_mrv=use_mrv)

    # 3. Try each colour in the variable's domain
    for colour in domains[var]:
        assignment[var] = colour

        # 4. If partial assignment is valid, search recursively
        if is_valid_assignment(assignment):
            result = backtracking_search(assignment, use_mrv=use_mrv)
            # 5. If solution found, return it
            if result is not None:
                return result

        # 6. Backtrack: remove temporary assignment
        del assignment[var]

    # 7. Fail if no colour works
    return None


# --------------------------------------------------
# TASK 4 — BRUTE FORCE COMPARISON
# --------------------------------------------------

# Six regions with three possible colours each give 3 ** 6 = 729
# complete assignments. Why can backtracking avoid checking all 729?

# Backtracking builds solutions incrementally and checks constraints on partial assignments at every step. 
# If a partial assignment violates a constraint (for example, if WA and NT are both assigned "Red" at step 2), 
# backtracking immediately halts that branch and discards it. 
# This single check prunes all 3 ** 4 = 81 possible complete assignments that would have stemmed from that invalid prefix, 
# saving the algorithm from ever having to generate or test them. 
# Brute force on the other hand, blindly generates and evaluates all 729 complete combinations regardless of early conflicts.

# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("WEEK 5 — CONSTRAINT SATISFACTION PROBLEMS")
    print("=" * 50)

    print("\nVariables:", variables)
    print("Domains:", domains)
    print("Constraints:", constraints)

    print("\nExample assignment valid?")
    print(is_valid_assignment(example_assignment))  # Expected: False

    partial_assignment = {"WA": "Red", "NT": "Green"}
    print("\nPartial assignment valid?")
    print(is_valid_assignment(partial_assignment))  # Expected: True

    print("\nSearching for a solution...")
    solution = backtracking_search({})
    print("Solution:", solution)

    if solution is not None:
        print("\nSolution valid?", is_valid_assignment(solution))
        print("\nColour assignment:")
        for region in variables:
            print(f"{region:4} -> {solution[region]}")
    else:
        print("No solution yet. Complete the TODO sections.")

    print("\nPossible complete assignments:", 3 ** len(variables))
    print("\nReflection:")
    print("1. What causes backtracking?")
    print("When an unassigned variable has no legal values remaining in its domain because every possible choice violates a constraint with its already assigned neighbours, causing the algorithm to undo the most recent assignment and try an alternative path")
    print("2. Why can backtracking be faster than brute force?")
    print("If assigning WA = Red and NT = Red fails early at step 2, backtracking immediately discards that entire branch, avoiding the 3 ** 4 = 81 complete solutions that would have stemmed from it. Brute force blindly generates and evaluates all 729 complete combinations regardless of early conflicts.")
    print("3. Why might MRV reduce search?")
    print("By prioritizing the variable with the fewest legal options left, MRV exposes dead-ends near the top of the search tree rather than deep down, drastically reducing the branching factor and saving search steps.")
    print("4. How could this model represent timetabling?")
    print("Timetabling can be modeled with lectures as variables, time-slot/room combinations as domains, and rules like no overlapping lecturers or rooms as constraints.")