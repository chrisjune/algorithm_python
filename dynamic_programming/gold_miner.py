cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    mine = []
    for i in range(n):
        mine.append(data[m * i:m * (i + 1)])

    result = [[0] * m for _ in range(n)]

    for i in range(n):
        result[i][0] = mine[i][0]

    for x in range(1, m):
        for y in range(0, n):
            candidate = []
            if 0 <= y - 1 < n and 0 <= x - 1 < m:
                candidate.append(result[y - 1][x - 1])
            if 0 <= y < n and 0 <= x - 1 < m:
                candidate.append(result[y][x - 1])
            if 0 <= y + 1 < n and 0 <= x - 1 < m:
                candidate.append(result[y + 1][x - 1])
            result[y][x] = max(*candidate) + mine[y][x]

    print(result)
    print(max([result[y][m - 1] for y in range(n)]))
