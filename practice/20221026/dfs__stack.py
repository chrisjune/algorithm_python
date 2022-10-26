from collections import deque

q = deque()

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9
q.append(1)
visited[1] = True


def dfs(graph, visited, start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

dfs(graph, visited, 1)