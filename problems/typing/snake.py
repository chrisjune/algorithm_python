n = int(input())
k = int(input())
map = []
for i in range(n):
    map.append([0] * n)

for i in range(k):
    y, x = input().split()
    map[int(y) - 1][int(x) - 1] = 1

t = int(input())
info = []
for i in range(t):
    d = input().split()
    info.append((int(d[0]), d[1]))

# 동남서북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 현재 방향에서 L/D에 따른 방향반환
def turn(c, i):
    if c == "D":
        i += 1
        if i == 4: i = 0
    else:
        i -= 1
        if i == -1: i = 3
    return i


# 초기변수
# 처음위치, 시간, 방향, 몸이 있는 좌표
s = 0, 0
time = 0
d = 0
body = [s]
while True:

    # 다음 이동할 위치
    ny = s[0] + dy[d]
    nx = s[1] + dx[d]

    if 0 <= ny <= n - 1 and 0 <= nx <= n - 1 and map[ny][nx] != 2:
        # 사과가 없는 칸이면 꼬리부터 삭제
        if map[ny][nx] == 0:
            tail = body.pop(0)
            map[tail[0]][tail[1]] = 0
        else:
            # 사과가 있는 칸이면 꼬리삭제 하지 않음
            print(1)
        # 머리가 이동하며 마킹
        map[ny][nx] = 2
        s = ny, nx
        body.append(s)

        # 시간이 지나면서 방향도는 요청에 맞는 시간이면 회전
        time += 1
        if len(info) >= 1 and info[0][0] == time:
            d = turn(info[0][1], d)
            info.pop(0)
    else:
        time += 1
        break
    # 테스트용 프린트
    for i in map:
        print(i)
    print("")

print(time)
