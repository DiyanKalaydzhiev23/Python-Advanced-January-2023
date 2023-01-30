def fill_the_box(height, length, width, *cubes):
    space = height * length * width
    cubes = list(cubes)

    while cubes[0] != "Finish":
        space -= cubes.pop(0)

        if space < 0:
            cubes_left = sum([x for x in cubes if x != "Finish"])
            return f"No more free space! You have {cubes_left + abs(space)} more cubes."

    return f"There is free space in the box. You could put {space} more cubes."
