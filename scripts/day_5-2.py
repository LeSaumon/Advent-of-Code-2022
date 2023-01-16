import os
import re

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def extract_data_from_move(move):
    crates_number, source, destination =  re.findall('[0-9]+', move)
    crates_number = int(crates_number)
    source = int(source) - 1
    destination = int(destination) - 1
    return  crates_number, source, destination

matrix = [
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
response = []


with open(ROOT_DIR + '/inputs/day_5.txt', 'r') as file:
    moves = file.read().splitlines()

    for move in moves:
        # Extract numbers value from move
        crates_number, source, destination = extract_data_from_move(move)

        # Take out crates from the source stack
        moving_crates = matrix[source][-crates_number:]
        matrix[source] = matrix[source][:-crates_number]

        # Add the moving crates to the destination stack
        matrix[destination].extend(moving_crates)

    with open(ROOT_DIR + '/outputs/day_5-2.txt', 'w')as answer:
        response = []
        for stack in matrix:
            response.append(stack[-1])
        answer.write("".join(response))
