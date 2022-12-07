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
    # Getting the elve with the higher calories values
    calories = max(elf["sum"] for elf in result.values())
