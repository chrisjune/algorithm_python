from collections import deque


def bfs(graph, number, visited):
    queue = deque([number])
    visited[number] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        near = graph[node]
        for n in near:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


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
bfs(graph, 1, visited)
