SIZE = 6

matrix = []
rover_pos = []

deposits = {
    "W": 0,
    "M": 0,
    "C": 0,
}

deposits_full_name = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    line = input().split()

    if "E" in line:
        rover_pos = [row, line.index("E")]

    matrix.append(line)

commands = input().split(", ")

for direction in commands:
    rover_pos[0] = directions[direction][0] + rover_pos[0]
    rover_pos[1] = directions[direction][1] + rover_pos[1]

    for i in range(len(rover_pos)):
        if rover_pos[i] < 0:
            rover_pos[i] = SIZE - 1
        elif rover_pos[i] == SIZE:
            rover_pos[i] = 0

    position = matrix[rover_pos[0]][rover_pos[1]]

    if position in deposits:
        print(f"{deposits_full_name[position]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        deposits[position] += 1
    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if all(deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
