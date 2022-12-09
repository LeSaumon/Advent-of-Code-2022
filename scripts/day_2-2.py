import os
import enum

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

class PlayerMove(enum.Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissor

class OpponentMove(enum.IntEnum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissor

class GameResults(enum.Enum):
    DEFEAT = 0
    DRAW = 3
    VICTORY = 6

RESULTS_CASES = {
    "VICTORY": {
        "A": PlayerMove.Y.value,
        "B": PlayerMove.Z.value,
        "C": PlayerMove.X.value,
        "POINTS": GameResults.VICTORY.value
    },
    "DEFEAT": {
        "A": PlayerMove.Z.value,
        "B": PlayerMove.X.value,
        "C": PlayerMove.Y.value,
        "POINTS": GameResults.DEFEAT.value

    },
    "DRAW": {
        "A": PlayerMove.X.value,
        "B": PlayerMove.Y.value,
        "C": PlayerMove.Z.value,
        "POINTS": GameResults.DRAW.value
    }
}

def detect_result(player_move):
    if player_move == PlayerMove.X.name:
        return GameResults.DEFEAT.name
    elif player_move == PlayerMove.Y.name:
        return GameResults.DRAW.name
    else:
        return GameResults.VICTORY.name

answers = []
with open(ROOT_DIR + '/inputs/day_2.txt') as game:

    for round in game:
        opponent_move = round[0]
        player_move = round[2]
        result = detect_result(player_move)
        answers.append(RESULTS_CASES[result]["POINTS"] + RESULTS_CASES[result][opponent_move])

    with open(ROOT_DIR + '/outputs/day_2-2.txt', "w") as output_file:
        output_file.write(str(sum(answers)))
