import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

with open(ROOT_DIR + '/inputs/day_1.txt') as file:
    result = {}

    # Get the numbers of lines of the file
    file_length = len(file.readlines()) - 1

    # Sending file pointer to start
    file.seek(0)
    elf = 0

    for count, line in enumerate(file):

        # Instantiate the data related to a single elf
        if f"Elf-{elf}" not in result:
            result[f"Elf-{elf}"] = {
                "values": []
            }

        # To split values between each elves
        if line == "\n" or count == file_length:
            result[f"Elf-{elf}"]["sum"] = sum(result[f"Elf-{elf}"]["values"])
            elf += 1

        else:
            result[f"Elf-{elf}"]["values"].append(int(line))

    # Build a list with all the sums of the elves
    elves_calories_sums = [value['sum'] for value in result.values()]
    top_3_elves_sums = []

    # Iterate over elves_calories_sums to extract the 3 maximum values
    for i in range(3):
        max_value = max(elves_calories_sums)
        top_3_elves_sums.append(max_value)
        # Delete the max_value to not get it the next iteration
        elves_calories_sums.pop(elves_calories_sums.index(max_value))

    with open(ROOT_DIR + '/outputs/day_1-2.txt', "w") as output_file:
        output_file.write(str(sum(top_3_elves_sums)))
