s = input()
length = len(s)

for step in range(1, len(s) // 2 + 1):
    compressed = ''
    prev = s[0:step]
    count = 1
    for i in range(step, len(s), step):
        now = s[i:i + step]
        if prev == now:
            count += 1
        else:
            compressed += str(count) + str(prev) if count > 1 else str(prev)
            prev = now
            count = 1

    compressed += str(count) + str(prev) if count > 1 else str(prev)
    length = min(length, len(compressed))
print(length)
