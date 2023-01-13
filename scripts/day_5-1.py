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
