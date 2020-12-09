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
    result = a_star(start_state, goal_state, comparator)
    # result = ids(start_state, goal_state)
    end = time.time()
    totaltime = end - start
    if result is None:
        print("No solution found")
    elif result == []:
        print("Start node was the goal!")
    else:
        print(result)
        print(f"{len(result)} moves")
    print(f"Total searching time: {round(totaltime, 5)} seconds")


if __name__ == "__main__":
    main()
