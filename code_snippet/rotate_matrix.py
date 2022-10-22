def rotate_matrix(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    new_matrix = [[0] * col_len for _ in range(row_len)]

    for r in range(row_len):
        for c in range(col_len):
            new_matrix[c][col_len - r - 1] = matrix[r][c]
    return new_matrix