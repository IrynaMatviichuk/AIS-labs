from Node import Node


def dls(start, goal, depth_limit):
    number_of_nodes_visited = 0
    max_number_of_nodes = 0
    number_of_nodes = 0
    number_of_explored = 0
    nodes = []
    explored = []
    nodes.append(Node.create_node(start, None, None, 0))
    while nodes:
        node = nodes.pop(0)
        number_of_nodes_visited += 1
        explored.append(node.get_state())
        print("trying state", node.state.get_matrix(), " and move: ", node.operator)
        if len(nodes) + len(explored) > max_number_of_nodes:
            max_number_of_nodes = len(nodes) + len(explored)
            number_of_nodes = len(nodes)
            number_of_explored = len(explored)

        if node.state == goal:
            return {
                "max_number_of_nodes": max_number_of_nodes,
                "number_of_nodes": number_of_nodes,
                "number_of_explored": number_of_explored,
                "number_of_nodes_visited": number_of_nodes_visited,
                "path_from_start": node.path_from_start(),
            }
        if node.depth < depth_limit:
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                if item.get_state() not in explored:
                    nodes.insert(0, item)


def ids(start, goal, depth_limit=50):
    for depth in range(depth_limit):
        result = dls(start, goal, depth)
        if result != None:
            return result
