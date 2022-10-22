matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]


def rotate_matrix(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    new_matrix = [[0] * col_len for _ in range(row_len)]

    for r in range(row_len):
        for c in range(col_len):
            new_matrix[c][col_len - r - 1] = matrix[r][c]
    return new_matrix


def check(new_lock):
    lock_length = len(new_lock)
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_matrix(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                    if check(new_lock) == True:
                        return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False
