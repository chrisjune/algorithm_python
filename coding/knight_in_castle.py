def run():
    position = input()
    column = ord(position[0]) - ord('a') + 1
    row = int(position[1])

    steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
    map_size = 8
    current = (column, row)
    count = 0
    for step in steps:
        if is_inside((current[0] + step[0], current[1] + step[1]), map_size):
            count += 1
    print(count)


def is_inside(position_tuple, size):
    if (position_tuple[0] > size or position_tuple[0] < 1): return False
    if (position_tuple[1] > size or position_tuple[1] < 1): return False
    return True


run()
