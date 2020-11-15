from State import move_up, move_down, move_left, move_right

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

    def getState(self):
        return self.state

    def getParent(self):
        return self.parent

    def getMoves(self):
        return self.operator

    def getCost(self):
        return self.cost

    def pathFromStart(self):
        stateList = []
        movesList = []
        currNode = self
        while currNode.getMoves() is not None:
            stateList.append(currNode.getState())
            movesList.append(currNode.getMoves())
            currNode = currNode.parent
        movesList.reverse()
        stateList.reverse()
        for state in stateList:
            self.display_board()
        return movesList

    def display_board(self):
        print("-------------")
        print("| %i | %i | %i |" % (self.state[0], self.state[1], self.state[2]))
        print("-------------")
        print("| %i | %i | %i |" % (self.state[3], self.state[4], self.state[5]))
        print("-------------")
        print("| %i | %i | %i |" % (self.state[6], self.state[7], self.state[8]))
        print("-------------")

    @staticmethod
    def create_node(state, parent, operator, depth, cost):
        return Node(state, parent, operator, depth, cost)

    @staticmethod
    def expand_node(node):
        """Returns a list of expanded nodes"""
        expanded_nodes = []
        expanded_nodes.append(
            Node.create_node(move_up(node.state), node, "up", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(move_down(node.state), node, "down", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(move_left(node.state), node, "left", node.depth + 1, 0)
        )
        expanded_nodes.append(
            Node.create_node(move_right(node.state), node, "right", node.depth + 1, 0)
        )
        # Filter the list and remove the nodes that are impossible (move function returned None)
        expanded_nodes = [
            node for node in expanded_nodes if node.state != None
        ]  # list comprehension!
        return expanded_nodes

