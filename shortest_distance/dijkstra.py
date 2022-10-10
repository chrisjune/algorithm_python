import sys

intput = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def djikstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = i[1] + distance[now]
            if cost < distance[i[0]]:
                distance[i[0]] = cost


djikstra(start)
for i in range(1, n + 1):
    if distance[i] == 'INF':
        print("Inf")
    else:
        print(distance[i])
