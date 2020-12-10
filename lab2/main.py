import functools
import time
from queue import PriorityQueue

from a_star_algorithm import a_star
from Comparator import Comparator
from ids_algorithm import ids
from Node import Node
from State import State


def main():
    start_state = State([
        0, 2, 3,
        4, 6, 1,
        7, 5, 8
    ])
    goal_state = State([
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    ])
    comparator = Comparator(goal_state)
    start = time.time()
    result = ids(start_state, goal_state)
    # result = a_star(start_state, goal_state, comparator)
    end = time.time()
    totaltime = end - start
    if result is None:
        print("No solution found")
    elif result == []:
        print("Start node was the goal!")
    else:
        print("The number of nodes visited", result.get("number_of_nodes_visited"))
        print("Max number of nodes stored in memory:", result.get("max_number_of_nodes"))
        print("including:")
        print("  ", result.get('number_of_explored'), "explored nodes")
        print("  ", result.get('number_of_nodes'), "nodes that have to be explored")
        print(f"Number of moves: {len(result.get('path_from_start'))}")
        print("States of moves are as follows:", result.get("path_from_start"))
    print(f"Total searching time: {round(totaltime, 5)} seconds")


if __name__ == "__main__":
    main()
