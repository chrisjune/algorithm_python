size = int(input())
triangle = []
for _ in range(size):
    triangle.append(list(map(int, input().split())))

result = [[0] * (size + 1) for _ in range(size)]
result[0][0] = triangle[0][0]

for y in range(size):
    for x in range(y + 1):
        result[y][x] = max(result[y - 1][x], result[y - 1][x - 1]) + triangle[y][x]

print(max([result[size - 1][x] for x in range(size)]))
