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
