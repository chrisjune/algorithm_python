from heapq import heappush, heappop, heapify

cards = [10, 50, 20, 40]

heapify(cards)

total = 0
while len(cards) > 1:
    min1 = heappop(cards)
    min2 = heappop(cards)
    sub = min1 + min2
    total += sub
    heappush(cards, sub)

print(total)