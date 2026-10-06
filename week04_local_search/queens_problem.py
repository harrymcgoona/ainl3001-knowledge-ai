from common.problem import Problem


class QueensProblem(Problem):
    """
    The N-Queens problem.

    A state is represented as a list.

    The index represents the column.
    The value represents the row containing the queen.

    Example:

        [0, 2, 1, 3]

    means:

        column 0 -> row 0
        column 1 -> row 2
        column 2 -> row 1
        column 3 -> row 3
    """

    def __init__(self, initial):
        super().__init__(initial, goal=None)

        self.n = len(initial)

    def actions(self, state):
        """
        Return all possible moves.

        An action is represented as:

            (column, new_row)
        """

        actions = []

        for column in range(self.n):

            current_row = state[column]

            for row in range(self.n):

                if row != current_row:
                    actions.append(
                        (column, row)
                    )

        return actions

    def result(self, state, action):
        """
        Return the board produced by applying an action.
        """

        column, new_row = action

        new_state = state.copy()
        new_state[column] = new_row

        return new_state

## MANUAL EXPLORATION

'''
for the state [0, 2, 1, 3]

Q . . .
. . Q .
. Q . .
. . . Q

1. Number of queens conflicts?
#1 (0, 0) and (3, 3)
#2 (1, 2) and (2, 1)

2. Is this a valid solution?
No. All queens must be safe from conflict.

3. Moves to lower conflict?
Moving (1, 2) to (1, 3) brings the conflicts down from 2 to 1 as it is no longer attacking (2, 1).
By the nature of the 4x4 grid there is no further moves that will reduce conflict as at least 1 queen will be next to or across from another.
'''