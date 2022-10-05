n, target = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coin_board = [10001] * 10001
coin_board[0] = 0  # 이게 진짜 중요한 코드임.

for coin in coins:
    for i in range(target + 1):
        prev = i - coin
        if prev < 0:
            continue

        coin_board[i] = min(coin_board[i], coin_board[prev] + 1)

print(coin_board[target] if coin_board[target] < 10001 else -1)
