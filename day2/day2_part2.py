from enum import IntEnum

WIN_SCORE = 6
DRAW_SCORE = 3
LOOSE_SCORE = 0


class Shapes(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


class Strategy(IntEnum):
    Win = 1
    Draw = 2
    Loose = 3


shapes_mapping = {
    "A": Shapes.Rock,
    "B": Shapes.Paper,
    "C": Shapes.Scissors
}

strategy_mapping = {
    "X": Strategy.Loose,
    "Y": Strategy.Draw,
    "Z": Strategy.Win
}

wins_with = {
    Shapes.Rock: Shapes.Scissors,
    Shapes.Paper: Shapes.Rock,
    Shapes.Scissors: Shapes.Paper
}

looses_with = {value: key for key, value in wins_with.items()}

result_score = 0


def extract_opponent_move_and_strategy(line):
    opponent_move, my_strategy = line.split()
    opponent_move = shapes_mapping[opponent_move]
    my_strategy = strategy_mapping[my_strategy]

    return opponent_move, my_strategy


def get_score_based_on_moves(my_move, opponent_move):
    if my_move == opponent_move:
        return DRAW_SCORE
    elif wins_with[my_move] == opponent_move:
        return WIN_SCORE
    else:
        return LOOSE_SCORE


def calculate_my_move(opponent_move, my_strategy):
    if my_strategy == Strategy.Draw:
        return opponent_move
    elif my_strategy == Strategy.Loose:
        return wins_with[opponent_move]
    else:
        return looses_with[opponent_move]


with open("input.txt", "r") as f:
    for line in f:
        opponent_move, my_strategy = extract_opponent_move_and_strategy(line)
        my_move = calculate_my_move(opponent_move, my_strategy)

        result_score += my_move
        result_score += get_score_based_on_moves(my_move, opponent_move)

print("Result", result_score)
