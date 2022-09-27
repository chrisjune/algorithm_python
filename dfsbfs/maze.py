from collections import deque

height, width = map(int, input().split())
graph = []
for h in range(height):
    graph.append(list(map(int, input())))


def maze():
    # [h, w]
    queue = deque()
    queue.append((0, 0))
    while queue:
        position = queue.popleft()
        # 상하좌우 값이 1이면 이전의 값을 더한다

        h = position[0]
        w = position[1]

        # 상하좌우
        dh = [-1, 1, 0, 0]
        dw = [0, 0, 1, -1]
        for i in range(len(dh)):
            nh = h + dh[i]
            nw = w + dw[i]
            if nh <= -1 or nh >= len(graph) or nw <= -1 or nw >= len(graph[0]):
                continue
            if graph[nh][nw] == 0:
                continue
            if graph[nh][nw] == 1:
                graph[nh][nw] += graph[h][w]
                queue.append((nh, nw))

    print(graph[len(graph)-1][len(graph[0])-1])
    print(graph)


maze()
