class Node:
    def __init__(self, state, parent, operator, depth, cost):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost
        # Contains the f-cost of this node from depth 0 for IDA_star search.
        self.f_cost = 0

    def get_state(self):
        return self.state

    def get_moves(self):
        return self.operator

    def path_from_start(self):
        state_list = []
        moves_list = []
        currNode = self
        while currNode.get_moves() is not None:
            state_list.append(currNode.get_state())
            moves_list.append(currNode.get_moves())
            currNode = currNode.parent
        moves_list.reverse()
        state_list.reverse()
        for state in state_list:
            self.display_board(state)
        return moves_list

    def display_board(self, state):
        matrix = state.get_matrix()
        print(f"| {matrix[0]} {matrix[1]} {matrix[2]} |")
        print(f"| {matrix[3]} {matrix[4]} {matrix[5]} |")
        print(f"| {matrix[6]} {matrix[7]} {matrix[8]} |")
        print()

    @staticmethod
    def create_node(state, parent, operator, depth, cost):
        return Node(state, parent, operator, depth, cost)

    @staticmethod
    def expand_node(node):
        """Returns a list of expanded nodes"""
        expanded_nodes = []
        expanded_nodes.append(
            Node.create_node(node.state.move_up(), node, "up", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_down(), node, "down", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_left(), node, "left", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(node.state.move_right(), node, "right", node.depth + 1, 0)
        )
        # Filter the list and remove the nodes that are impossible (move function returned None)
        expanded_nodes = [
            node for node in expanded_nodes if node.state != None
        ]  # list comprehension!
        return expanded_nodes
