

def dfs(graph, number, visited):
    print(number, end=' ')
    visited[number] = True
    for n in graph[number]:
        if not visited[n]:
            dfs(graph, n, visited)


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
dfs(graph, 1, visited)
