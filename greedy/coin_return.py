remain = 1260
coin_type = [500, 100, 50, 10]
coin_count = 0
for coin in coin_type:
    coin_count = coin_count + remain // coin
    remain = remain % coin

print(coin_count)
