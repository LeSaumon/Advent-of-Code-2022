# Il semble qu'il y ait encore pas mal de travail en double de prévu.
# Au lieu de cela, les Elfes aimeraient connaître le nombre de paires qui se chevauchent tout court.

# Dans l'exemple ci-dessus, les deux premières paires (2-4,6-8 et 2-3,4-5)
# ne se chevauchent pas, tandis que les quatre autres paires (5-7,7-9, 2-8,3-7, 6-6,4-6 et 2-6,4-8)
# se chevauchent :

#     5-7,7-9 se chevauche dans une seule section, 7.
#     2-8,3-7 chevauche toutes les sections 3 à 7.
#     6-6,4-6 se chevauche dans une seule section, 6.
#     2-6,4-8 chevauche les sections 4, 5 et 6.

# Ainsi, dans cet exemple, le nombre de paires d'affectations qui se chevauchent est de 4.

# Dans combien de paires d'affectations les plages se chevauchent-elles ?


import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def transform_range_in_set(start, end):
    return set(range(int(start), int(end ) + 1))


with open(ROOT_DIR + '/inputs/day_4.txt') as file:
    ranges_input = file.read().splitlines()
    ranges = [range.split(',') for range in ranges_input]
    intersected = 0
    processed_ranges = [
        (
            transform_range_in_set(range[0].split('-')[0], range[0].split('-')[1]),
            transform_range_in_set(range[1].split('-')[0],range[1].split('-')[1])
        ) for range in ranges]

    for range in processed_ranges:
        # Detect if there is an intersection between the two ranges
        if range[0].intersection(range[1]) or range[1].intersection(range[0]):
            intersected += 1

    with open(ROOT_DIR + '/outputs/day_4-2.txt', "w") as solution:
        solution.write(str(intersected))
