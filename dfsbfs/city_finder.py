from collections import deque

n, m, k, x = 4, 4, 2, 1
# maps = [
#     [1, 2],
#     [1, 3],
#     [2, 3],
#     [2, 4]
# ]

maps = [
    [],
    [2, 3],
    [3, 4],
    [],
    []
]

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([1])
dist = [m + 1] * (n + 1)
dist[x] = 0

while q:
    popped = q.popleft()
    for i in maps[popped]:
        dist[i] = min(dist[i], dist[popped] + 1)
        q.append(i)

print(dist)