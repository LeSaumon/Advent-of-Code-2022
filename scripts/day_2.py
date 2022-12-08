# Les Elfes commencent à installer leur camp sur la plage.
# Pour décider quelle tente sera la plus proche de la réserve de snacks, un tournoi géant de Pierre Papier Ciseaux est déjà en cours.

# Chaque partie comporte plusieurs manches ; à chaque manche, les joueurs choisissent simultanément l'une des options suivantes :
# Pierre Papier Ciseaux, en utilisant une forme de main.
# Ensuite, un gagnant est désigné pour ce tour : La pierre bat les ciseaux, les ciseaux battent le papier et le papier bat la pierre.
#  Si les deux joueurs choisissent la même forme, le tour se termine par un match nul.

# En guise de remerciement pour votre aide d'hier, un Elfe vous donne un guide stratégique crypté (votre entrée de puzzle)
#  qui, selon lui, vous aidera à gagner.
#  "La première colonne indique ce que votre adversaire va jouer : A pour Pierre, B pour Papier, et C pour Ciseaux. La deuxième colonne..."
#  Soudain, l'elfe est appelé à l'aide pour la tente de quelqu'un.

# Vous vous dites que la deuxième colonne doit être ce que vous devez jouer en réponse : X pour Pierre,
#  Y pour Papier, et Z pour Ciseaux. Gagner à chaque fois serait suspect,
# les réponses doivent donc avoir été soigneusement choisies.

# Le gagnant de l'ensemble du tournoi est le joueur qui a le score le plus élevé.
# Votre score total est la somme de vos scores pour chaque tour.
# Le score d'un tour est le score de la forme que vous avez choisie (1 pour Pierre Papier Ciseaux, 2 pour Papier Ciseaux et 3 pour Ciseaux)
# plus le score du résultat du tour (0 si vous avez perdu, 3 si le tour est nul et 6 si vous avez gagné).

# Comme vous ne pouvez pas savoir si le lutin essaie de vous aider ou de vous piéger,
# vous devez calculer le score que vous obtiendriez si vous suiviez le guide de stratégie.

# Par exemple, supposons que l'on vous donne le guide stratégique suivant :

# A Y
# B X
# C Z

# Ce guide de stratégie prédit et recommande ce qui suit :

#     Au premier tour, votre adversaire choisira Rock (A), et vous devriez choisir Paper (Y).
#  Vous gagnez avec un score de 8 (2 parce que vous avez choisi Papier + 6 parce que vous avez gagné).
#     Au deuxième tour, votre adversaire choisira le papier (B), et vous devriez choisir la pierre (X).
# Vous perdez donc avec un score de 1 (1 + 0).
#     Le troisième tour est un match nul, les deux joueurs choisissant les ciseaux, ce qui vous donne un score de 3 + 3 = 6.

# Dans cet exemple, si vous aviez suivi le guide de stratégie, vous auriez obtenu un score total de 15 (8 + 1 + 6).

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
