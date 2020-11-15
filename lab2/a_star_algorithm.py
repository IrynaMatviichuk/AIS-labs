import functools

from Node import Node


def a_star(start, goal, comparator):
    """Perfoms the A* heuristic search"""
    nodes = []
    nodes.append(Node.create_node(start, None, None, 0, 0))
    explored = []
    count = 0
    while nodes:
        # Sort the nodes with custom compare function.
        nodes.sort(key=functools.cmp_to_key(comparator.cmp))
        # take the node from the front of the queue
        node = nodes.pop(0)
        explored.append(node.get_state())
        count += 1
        # if this node is the goal, return the moves it took to get here.
        print("Trying state", node.state.get_matrix(), " and move: ", node.operator)
        if node.state == goal:
            print("done")
            print("The number of nodes visited", count)
            print("States of moves are as follows:")
            return node.path_from_start()
        else:
            # Expand the node and add all the expansions to the end of the queue
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                state = item.get_state()
                if state not in explored:
                    nodes.append(item)
