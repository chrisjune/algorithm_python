# 맵사이즈, 위치(방향), 맵정보를 입력받는다

# 데이터구조
# 1. 맵구조, 2. 방문한맵을 마킹 ( 맵자체에 숫자를 변경하는건 금지)
# 3. 방향은 다음탐색할 방향의 칸을 결정할 수 있음 dx, dy

height, width = map(int, input().split())
visited = []
for _ in range(height):
    visited.append([0 for _ in range(width)])
print(visited)

y, x, direction = map(int, input().split())

land = []
for _ in range(height):
    land.append(list(map(int, input().split())))
print(land)

position = (x, y)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


visit_count = 1
turn_times = 0
while True:
    turn_left()
    ix = position[0] + dx[direction]
    iy = position[1] + dy[direction]
    print(f"ix:{ix}, iy: {iy}, value:{land[iy][ix]}")

    if visited[iy][ix] == 0 and land[iy][ix] == 0:
        visit_count += 1
        position = (ix, iy)
        visited[iy][ix] = 1
        continue
    else:
        turn_times += 1

    if turn_times == 4:
        ix = position[0] - dx[direction]
        iy = position[1] - dy[direction]
        if land[iy][ix] == 0:
            position = (ix, iy)

        if land[iy][ix] == 1:
            break
print(visit_count)
