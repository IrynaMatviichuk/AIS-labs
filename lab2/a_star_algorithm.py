import functools

from Node import Node


def a_star(start, goal, comparator):
    nodes = []
    nodes.append(Node.create_node(start, None, None, 0))
    explored = []
    count = 0
    while nodes:
        nodes.sort(key=functools.cmp_to_key(comparator.cmp))
        node = nodes.pop(0)
        explored.append(node.get_state())
        count += 1
        print("trying state", node.state.get_matrix(), " and move: ", node.operator)
        if node.state == goal:
            print("The number of nodes visited", count)
            print("States of moves are as follows:")
            return node.path_from_start()
        else:
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                state = item.get_state()
                if state not in explored:
                    nodes.append(item)
