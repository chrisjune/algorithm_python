# n = int(input())
# cards = [10,20,40]
cards = [10, 20 ,40,50]

cards.sort()

total = 0
sub = 10
for i in range(1, len(cards)):
    sub = sub + cards[i]
    total += sub
print(total)

