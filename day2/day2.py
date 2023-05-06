from enum import IntEnum

WIN_SCORE = 6
DRAW_SCORE = 3
LOOSE_SCORE = 0


class Shapes(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


shapes_mapping = {
    "A": Shapes.Rock,
    "B": Shapes.Paper,
    "C": Shapes.Scissors,
    "X": Shapes.Rock,
    "Y": Shapes.Paper,
    "Z": Shapes.Scissors
}

wins_with = {
    Shapes.Rock: Shapes.Scissors,
    Shapes.Paper: Shapes.Rock,
    Shapes.Scissors: Shapes.Paper
}

result_score = 0


def extract_moves_from_input(line):
    opponent_move, my_move = line.split()
    opponent_move = shapes_mapping[opponent_move]
    my_move = shapes_mapping[my_move]
    return opponent_move, my_move


def get_score_based_on_moves(my_move, opponent_move):
    if my_move == opponent_move:
        return DRAW_SCORE
    elif wins_with[my_move] == opponent_move:
        return WIN_SCORE
    else:
        return LOOSE_SCORE


with open("input.txt", "r") as f:
    for line in f:
        opponent_move, my_move = extract_moves_from_input(line)
        result_score += my_move
        result_score += get_score_based_on_moves(my_move, opponent_move)

print("Result", result_score)
