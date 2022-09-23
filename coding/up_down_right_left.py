size = int(input())
commands = input().split()

# L R U D 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
command_name = ["L", "R", "U", "D"]

# initial position
x, y = 1, 1
for command in commands:
    nx, ny = x, y
    for i in range(len(command_name)):
        if command_name[i] == command:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > size or ny < 1 or ny > size:
        continue
    x, y = nx, ny

print(x, y)
