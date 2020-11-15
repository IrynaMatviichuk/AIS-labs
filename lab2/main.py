import time
import functools

from queue import PriorityQueue

from Node import Node

goal_state = [1,2,3,4,5,6,7,8,0]

INFINITY = 50000
maxnodes = 1


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
        explored.append(node.getState())
        print("Trying state", node.state, " and move: ", node.operator)
        # if this node is the goal, return the moves it took to get here.
        if node.state == goal:
            print("done")
            print("The number of nodes visited", count)
            print("States of moves are as follows:")
            return node.pathFromStart()
        if node.depth < depth_limit:
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                state = item.getState()
                if state not in explored:
                    nodes.insert(0, item)


def ids(start, goal, depth=50):
    """Perfoms an iterative depth first search."""
    for i in range(depth):
        result = dls(start, goal, i)
        if result != None:
            return result


def a_star(start, goal):
    """Perfoms the A* heuristic search"""
    nodes = []
    nodes.append(Node.create_node(start, None, None, 0, 0))
    explored = []
    count = 0
    while nodes:
        # Sort the nodes with custom compare function.
        nodes.sort(key=functools.cmp_to_key(cmp))
        # sorted(nodes, cmp=cmp)
        # take the node from the front of the queue
        node = nodes.pop(0)
        explored.append(node.getState())
        count += 1
        # if this node is the goal, return the moves it took to get here.
        print("Trying state", node.state, " and move: ", node.operator)
        if node.state == goal:
            print("done")
            print("The number of nodes visited", count)
            print("States of moves are as follows:")
            return node.pathFromStart()
        else:
            # Expand the node and add all the expansions to the end of the queue
            expanded_nodes = Node.expand_node(node)
            for item in expanded_nodes:
                state = item.getState()
                if state not in explored:
                    nodes.append(item)

def cmp(x, y):
    """Compare function for A* and IDA*."""
    # f1,using h1(number of tiles out of place)
    # return f1(x) - f1(y)

    # f2,using h2(sum of manhattan distance)
    return f1(x) - f1(y)

def h1(state, goal):
    """Heuristic. Returns an integer based on out of place tiles"""
    cost = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            cost += 1
    return cost

def f1(node):
    """ f(n) = g(n) + h(n). use depth (number of moves) for g(n)."""
    # using h1(number of tiles out of place)
    return node.depth + h1(node.state, goal_state)

# Main method
def main():
    # start_state=[1,3,4,8,6,2,7,0,5] [2,8,1,0,4,3,7,6,5] [5,6,7,4,0,8,3,2,1]
    start_state = [1,2,3,0,4,6,7,5,8]
    ### CHANGE THIS FUNCTION TO USE bfs, dfs, dls, ids, greedy, a_star or ida_star
    start = time.time()
    result = a_star(start_state, goal_state)
    end = time.time()
    totaltime = end - start
    if result == None:
        print("No solution found")
    elif result == [None]:
        print("Start node was the goal!")
    else:
        print(result)
        print(len(result), " moves")
    print("Total searching time: %.5f seconds" % (totaltime))



if __name__ == "__main__":
    main()
