map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
# y, x
head = [0, 0]
tail = [0, 0]
command = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
    'N': [0, 0]
}
loop_count = 0

direction = 'R'
command_list = ['N', 'N', 'D', 'R', 'D', 'R','D', 'R', 'D']

while True:
    loop_count += 1
    if command_list[loop_count] != 'N':
        direction = command_list[loop_count]

    com = command[direction]
    nh = [head[0] + com[0], head[1] + com[1]]
    print(nh)
    if nh[0] < 0 or nh[0] >= len(map) or nh[1] < 0 or nh[1] >= len(map):
        break

    head = nh
print(map)
print(loop_count)
