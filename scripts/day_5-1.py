# # # # L'expédition peut partir dès que les dernières fournitures ont été déchargées des navires.
# # # # Les fournitures sont stockées dans des piles de caisses marquées, mais comme les fournitures nécessaires
# # # # sont enfouies sous de nombreuses autres caisses, celles-ci doivent être réorganisées.

# # # # Le navire est équipé d'une grue géante capable de déplacer les caisses entre les piles.
# # # # Pour s'assurer qu'aucune caisse ne soit écrasée ou ne tombe, le grutier les réarrange en une série d'étapes soigneusement planifiées.
# # # # Une fois les caisses réarrangées, les caisses souhaitées se trouveront en haut de chaque pile.

# # # # Les Elfes ne veulent pas interrompre le grutier pendant cette procédure délicate,
# # # # mais ils ont oublié de lui demander quelle caisse se retrouvera à quel endroit,
# # # # et ils veulent être prêts à les décharger dès que possible pour pouvoir embarquer.

# # # # Ils disposent toutefois d'un dessin des piles de caisses de départ et de la procédure de réarrangement (votre contribution au puzzle).
# # # #  Par exemple :

# # # #     [D]
# # # # [N] [C]
# # # # [Z] [M] [P]
# # # #  1   2   3

# # # # move 1 from 2 to 1
# # # # move 3 from 1 to 3
# # # # move 2 from 2 to 1
# # # # move 1 from 1 to 2

# # # # Dans cet exemple, il y a trois piles de caisses. La pile 1 contient deux caisses : la caisse Z est en bas et la caisse N est en haut.
# # # # La pile 2 contient trois caisses ; de bas en haut, ce sont les caisses M, C et D.
# # # # Enfin, la pile 3 contient une seule caisse, P.

# # # # Ensuite, la procédure de réarrangement est donnée.
# # # # À chaque étape de la procédure, une quantité de casiers est déplacée d'une pile à une autre.
# # # # Lors de la première étape de la procédure de réarrangement ci-dessus, une caisse est déplacée de la pile 2 à la pile 1,
# # # #  ce qui donne la configuration suivante :

# # # # [D]
# # # # [N] [C]
# # # # [Z] [M] [P]
# # # #  1   2   3

# # # Dans la deuxième étape, trois caisses sont déplacées de la pile 1 à la pile 3.
# # # Les caisses sont déplacées une par une, de sorte que la première caisse à être déplacée (D)
# # #  se retrouve sous les deuxième et troisième caisses :

# # #         [Z]
# # #         [N]
# # #     [C] [D]
# # #     [M] [P]
# # #  1   2   3

# # Ensuite, les deux caisses sont déplacées de la pile 2 à la pile 1.
# # Encore une fois, comme les caisses sont déplacées une par une, la caisse C se retrouve sous la caisse M :

# #         [Z]
# #         [N]
# # [M]     [D]
# # [C]     [P]
# #  1   2   3

# # Enfin, une caisse est déplacée de la pile 1 à la pile 2 :
# #         [Z]
# #         [N]
# #         [D]
# # [C] [M] [P]
# #  1   2   3

# Les lutins ont juste besoin de savoir quelle caisse se retrouvera sur le dessus de chaque pile ;
# dans cet exemple, les caisses du dessus sont C dans la pile 1, M dans la pile 2 et Z dans la pile 3,
# vous devez donc les combiner ensemble et donner aux lutins le message CMZ.

# Une fois la procédure de réorganisation terminée, quelle caisse se retrouve en haut de chaque pile ?

from collections import deque
import os
import re

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
def extract_data_from_move(move):
    return re.findall('[0-9]+', move)
matrix_input = [
    ["S", "L", "W"],
    ["J", "T", "N", "Q"],
    ["S", "C", "H", "F", "J"],
    ["T", "R", "M", "W", "N", "G", "B"],
    ["T", "R", "L", "S", "D", "H", "Q", "B"],
    ["M", "J", "B", "V", "F", "H", "R", "L"],
    ["D", "W", "R", "N", "J", "M"],
    ["B", "Z", "T", "F", "H", "N", "D", "J"],
    ["H", "L", "Q", "N", "B", "F", "T"],
]
matrix_dict = {}
response = []


for index, rows in enumerate(matrix_input, 0):
    matrix_dict[index + 1] = deque(matrix_input[index])

with open(ROOT_DIR + '/inputs/day_5.txt') as file:
    moves = file.read().splitlines()
    for move in moves:
        crates_iterator, source, destination = extract_data_from_move(move)

        for crate in range(int(crates_iterator)):
            moving_crate = matrix_dict[int(source)].pop()
            matrix_dict[int(destination)].append(moving_crate)

    for stack in matrix_dict:
        response.append(matrix_dict[stack].pop())

    with open(ROOT_DIR + "/outputs/day_5-1.txt", "w") as solution:
        print("".join(response))
