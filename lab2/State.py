class State:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if isinstance(other, State):
            return self.matrix == other.matrix
        else:
            return False

    def get_matrix(self):
        return self.matrix

    def move_up(self):
        """Moves the blank tile up on the board. Returns a new state as a list."""
        new_state = self.matrix[:]
        index = new_state.index(0)
        if index not in [0, 1, 2]:
            temp = new_state[index - 3]
            new_state[index - 3] = new_state[index]
            new_state[index] = temp
            return State(new_state)
        else:
            return None

    def move_down(self):
        """Moves the blank tile down on the board. Returns a new state as a list."""
        new_state = self.matrix[:]
        index = new_state.index(0)
        if index not in [6, 7, 8]:
            temp = new_state[index + 3]
            new_state[index + 3] = new_state[index]
            new_state[index] = temp
            return State(new_state)
        else:
            return None

    def move_left(self):
        """Moves the blank tile left on the board. Returns a new state as a list."""
        new_state = self.matrix[:]
        index = new_state.index(0)
        if index not in [0, 3, 6]:
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return State(new_state)
        else:
            return None

    def move_right(self):
        """Moves the blank tile right on the board. Returns a new state as a list."""
        new_state = self.matrix[:]
        index = new_state.index(0)
        if index not in [2, 5, 8]:
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return State(new_state)
        else:
            return None
