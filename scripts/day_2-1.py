import os
import enum

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

class PlayerMove(enum.Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissor

    @staticmethod
    def get_point_from_move(move) -> int:
        if move == PlayerMove.X.name:
            return PlayerMove.X.value
        elif move == PlayerMove.Y.name:
            return PlayerMove.Y.value
        else:
            return PlayerMove.Z.value

class OpponentMove(enum.IntEnum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissor

class GameResults(enum.Enum):
    DEFEAT = 0
    DRAW = 3
    VICTORY = 6

def detect_results(player_move, opponent_move) -> int:
    # Handle the Rock move
    if player_move == PlayerMove.X.name:
        # Loose
        if opponent_move == OpponentMove.B.name:
            return GameResults.DEFEAT.value + PlayerMove.get_point_from_move(player_move)
        # Win
        elif opponent_move == OpponentMove.C.name:
            return GameResults.VICTORY.value + PlayerMove.get_point_from_move(player_move)

    #  Handle the Paper Move
    if player_move == PlayerMove.Y.name:
        # Loose
        if opponent_move == OpponentMove.C.name:
            return GameResults.DEFEAT.value + PlayerMove.get_point_from_move(player_move)
        # Win
        elif opponent_move == OpponentMove.A.name:
            return GameResults.VICTORY.value + PlayerMove.get_point_from_move(player_move)

        #  Handle the Scissor Move
    if player_move == PlayerMove.Z.name:
        # Loose
        if opponent_move == OpponentMove.A.name:
            return GameResults.DEFEAT.value + PlayerMove.get_point_from_move(player_move)
        # Win
        elif opponent_move == OpponentMove.B.name:
            return GameResults.VICTORY.value + PlayerMove.get_point_from_move(player_move)

    return GameResults.DRAW.value + PlayerMove.get_point_from_move(player_move)

answers = []
with open(ROOT_DIR + '/inputs/day_2.txt') as game:

    for round in game:
        opponent_move = round[0]
        player_move = round[2]
        result = detect_results(player_move, opponent_move)
        answers.append(result)

    with open(ROOT_DIR + '/outputs/day_2-1.txt', "w") as output_file:
        output_file.write(str(sum(answers)))
