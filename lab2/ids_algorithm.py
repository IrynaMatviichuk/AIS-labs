from Node import Node


def dls(start, goal, depth=20):
    """Performs the depth limit search. """
    depth_limit = depth
    # A list (can act as a stack too) for the nodes.
    nodes = []
    # Create the queue with the root node in it.
    nodes.append(Node.create_node(start, None, None, 0, 0))
    count = 0
    explored = []
    while nodes:
        # take the node from the front of the queue
        node = nodes.pop(0)
        count += 1
        explored.append(node.get_state())
        print("Trying state", node.state.get_matrix(), " and move: ", node.operator)
        # if this node is the goal, return the moves it took to get here.
        if node.state == goal:
            print("done")
            print("The number of nodes visited", count)
            print("States of moves are as follows:")
            return node.path_from_start()
        if node.depth < depth_limit:
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                state = item.get_state()
                if state not in explored:
                    nodes.insert(0, item)


def ids(start, goal, depth=50):
    """Perfoms an iterative depth first search."""
    for i in range(depth):
        result = dls(start, goal, i)
        if result != None:
            return result
