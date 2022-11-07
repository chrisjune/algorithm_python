# [0,0,0,0], []

INF = 1e9
maxvalue = -INF
minvalue = INF

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


def dfs(i, now):
    global maxvalue, minvalue, add, sub, mul, div
    global minvalue
    if i == n:
        maxvalue = max(maxvalue, now)
        minvalue = min(minvalue, now)
    else:
        if add:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div:
            div -= 1
            dfs(i + 1, now / data[i])
            div += 1


dfs(1, data[0])
print(maxvalue)
print(minvalue)
