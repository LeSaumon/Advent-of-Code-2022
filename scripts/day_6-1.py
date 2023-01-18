import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def detect_siblings_in_string(string: str):
    for char in string:
        if string.count(char) > 1:
            return True
    return False

with open(ROOT_DIR + "/inputs/day_6.txt", "r") as file:
    input = file.read()
    for response, char in enumerate(input, 1):
        if detect_siblings_in_string(input[:4]):
            input = input[1:]
        else:
            with open(ROOT_DIR + "/outputs/day_6-1.txt", "w")as answer:
                answer.write(str(response - 3))
            break
