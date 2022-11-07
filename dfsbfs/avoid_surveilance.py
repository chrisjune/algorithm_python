map = [
    ['S', 'S', 'S', 'T'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['T', 'T', 'T', 'X'],
]

count = 3


def can_hide(new_map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if new_map[y][x] == 'S':
                # 상하좌우
                for ny in range(y - 1, 0 - 1, -1):
                    if new_map[ny][x] == 'O':
                        break
                    elif new_map[ny][x] == 'T':
                        return False
                    else:
                        continue
                for ny in range(y + 1, len(map)):
                    if new_map[ny][x] == 'O':
                        break
                    elif new_map[ny][x] == 'T':
                        return False
                    else:
                        continue
                for nx in range(x - 1, 0 - 1, -1):
                    if new_map[y][nx] == 'O':
                        break
                    elif new_map[y][nx] == 'T':
                        return False
                    else:
                        continue
                for nx in range(x + 1, len(new_map[0])):
                    if new_map[y][nx] == 'O':
                        break
                    elif new_map[y][nx] == 'T':
                        return False
                    else:
                        continue
    return True


def dfs(opts):
    if opts == 0:
        return can_hide(map)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'X':
                map[y][x] = 'O'
                if dfs(opts - 1):
                    return True
                map[y][x] = 'X'

    return False


print(dfs(count))
