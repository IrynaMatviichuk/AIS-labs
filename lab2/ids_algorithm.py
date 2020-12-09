from Node import Node


def dls(start, goal, depth=20):
    depth_limit = depth
    nodes = []
    nodes.append(Node.create_node(start, None, None, 0))
    count = 0
    explored = []
    while nodes:
        node = nodes.pop(0)
        count += 1
        explored.append(node.get_state())
        print("trying state", node.state.get_matrix(), " and move: ", node.operator)
        if node.state == goal:
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
    for i in range(depth):
        result = dls(start, goal, i)
        if result != None:
            return result
