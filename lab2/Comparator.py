class Comparator:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def cmp(self, x, y):
        return self.f(x) - self.f(y)

    def h1(self, state):
        state = state.get_matrix()
        goal = self.goal_state.get_matrix()
        cost = 0
        for i in range(len(state)):
            if state[i] != goal[i]:
                cost += 1
        return cost

    def f(self, node):
        return node.depth + self.h1(node.state)
