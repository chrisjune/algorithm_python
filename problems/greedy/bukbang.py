import heapq

def solution(food_times, k):
    foods = food_times
    if sum(foods) <= k:
        return -1

    q = []
    length = len(foods)
    for i in range(len(foods)):
        heapq.heappush(q, (foods[i], i + 1))

    sub = 0
    pre = 0

    while sub + ((q[0][0] - pre) * length) <= k:
        now = heapq.heappop(q)[0]
        sub += (now - pre) * length
        length -= 1
        pre = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sub) % length][1]