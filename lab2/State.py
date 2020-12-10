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
        new_state = self.matrix[:]
        index = new_state.index(0)
        if index not in [2, 5, 8]:
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return State(new_state)
        else:
            return None

    def display_board(self):
        matrix = self.get_matrix()
        print(f"| {matrix[0]} {matrix[1]} {matrix[2]} |")
        print(f"| {matrix[3]} {matrix[4]} {matrix[5]} |")
        print(f"| {matrix[6]} {matrix[7]} {matrix[8]} |")
