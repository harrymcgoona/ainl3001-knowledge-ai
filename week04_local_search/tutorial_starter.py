"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Create an empty list of actions.
        # 3. Check which movements are valid.
        # 4. Add valid actions to the list.
        # 5. Return the list.

        x, y = state
        valid_actions=[]

        # UP
        if y > 0:
            valid_actions.append("UP")
        # DOWN
        if y < GRID_SIZE - 1:
            valid_actions.append("DOWN") 
        # LEFT
        if x > 0:
            valid_actions.append("LEFT")
        # RIGHT
        if x < GRID_SIZE - 1:
            valid_actions.append("RIGHT")

        return valid_actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Check which action was requested.
        # 3. Return the resulting state.

        x, y = state

        if action == "UP":
            return (x, y - 1)
        elif action == "DOWN":
            return (x, y + 1)
        elif action == "LEFT":
            return (x - 1, y)
        elif action == "RIGHT":
            return (x + 1, y)

        return state


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


# --------------------------------------------------
# REFLECTION QUESTIONS
# --------------------------------------------------

"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """
        x, y = state
        valid_actions = []

        # UP decreases y coordinate (cannot go below 0)
        if y > 0:
            valid_actions.append("UP")

        # DOWN increases y coordinate (cannot exceed GRID_SIZE - 1)
        if y < GRID_SIZE - 1:
            valid_actions.append("DOWN")

        # LEFT decreases x coordinate (cannot go below 0)
        if x > 0:
            valid_actions.append("LEFT")

        # RIGHT increases x coordinate (cannot exceed GRID_SIZE - 1)
        if x < GRID_SIZE - 1:
            valid_actions.append("RIGHT")

        return valid_actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """
        x, y = state

        if action == "UP":
            return (x, y - 1)
        elif action == "DOWN":
            return (x, y + 1)
        elif action == "LEFT":
            return (x - 1, y)
        elif action == "RIGHT":
            return (x + 1, y)

        return state


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


"""
Be ready to discuss:

1. What information is stored in problem.initial?
Answer. The starting state of the problem, (0, 0).

2. What information is stored in problem.goal?
Answer. The target state we want to reach (4, 4).

3. What is the difference between:

       problem.actions(state)

   and:

       problem.result(state, action)
Answer. actions(state) is used to ask what moves are legal and returns a list of choices (e.g., [UP, DOWN]).
        result(state) is used to ask where the piece lands if it moves in a specified direction and returns a new state (e.g., (1, 0)).

4. Why doesn't Problem know anything about grids?
Answer. It's an abstract base class designed to enforce a common structure and separate the general AI architecture from specic problem rules.

5. Why doesn't GridProblem know anything about search?
Answer. Only defines how nodes connect and move.

6. Could the same Problem structure be used for something
   other than a grid?
Answer. Yes, it works for N-Queens whose state is a list.
"""