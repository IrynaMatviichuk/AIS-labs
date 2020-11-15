class Comparator:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def cmp(self, x, y):
        """Compare function for A* and IDA*."""
        return self.f(x) - self.f(y)

    def h1(self, state):
        """Heuristic. Returns an integer based on out of place tiles"""
        state = state.get_matrix()
        goal = self.goal_state.get_matrix()
        cost = 0
        for i in range(len(state)):
            if state[i] != goal[i]:
                cost += 1
        return cost

    def f(self, node):
        """ f(n) = g(n) + h(n). use depth (number of moves) for g(n)."""
        return node.depth + self.h1(node.state)
