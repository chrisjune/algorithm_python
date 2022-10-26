n = int(input())
commands = input().split()

c = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0]
}
position = (1, 1)
for i in range(len(commands)):

    ny = position[0] + c[commands[i]][0]
    nx = position[1] + c[commands[i]][1]
    if 1 <= ny <= n and 1 <= nx <= n:
        position = (ny, nx)
print(position)
