height, width = map(int, input().split())
tray = []
for h in range(height):
    tray.append(list(map(int, input())))


def dfs(tray, h, w):
    # 상하좌우
    if h <= -1 or h >= len(tray) or w <= -1 or w >= len(tray[0]):
        return False

    if tray[h][w] == 0:
        tray[h][w] = 1
        dfs(tray, h - 1, w)
        dfs(tray, h + 1, w)
        dfs(tray, h, w + 1)
        dfs(tray, h, w - 1)
        return True
    return False


count = 0
for h in range(height):
    for w in range(width):
        count += dfs(tray, h, w)
print(count)
