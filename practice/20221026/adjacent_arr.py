INF = 987654321
matrix = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# ==>?

array =[
    [0,1,7],
    [0,2,5],
    [1,0,7],
    [2,0,5],
]

# --->

array2 = [[] for _ in range(3)]

# 노드, 거리
array2[0].append([1,7])
array2[0].append([2,5])

array2[1].append([0,7])
array2[2].append([0, 5])
print(array2)
