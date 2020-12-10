import random

from State import State

INITIAL_BOARD = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]
NUMBER_OF_MOVES = 5
MOVES = {
    1: "move_up",
    -1: "move_down",
    2: "move_left",
    -2: "move_right",
}


def generate_board():
    state = State(INITIAL_BOARD)
    current_number_of_moves = 0
    previous_move = 0
    movements_made = []

    while current_number_of_moves < NUMBER_OF_MOVES:
        move = random.choice(list(MOVES.keys()))
        if not move + previous_move == 0:
            new_state = getattr(state, MOVES[move])()
            if new_state is not None:
                state = new_state
                current_number_of_moves += 1
                previous_move = move
                movements_made.append(MOVES[move].split("_")[-1])
                print(MOVES[move])
                state.display_board()
                print()

    print("NUMBER_OF_MOVES:", NUMBER_OF_MOVES)
    print("MOVEMENTS_MADE:", movements_made)
    return state.get_matrix()


generated_board = generate_board()
print("GENERATED BOARD:", generated_board)
