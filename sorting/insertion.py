array = [7, 5, 0, 3, 1, 6, 2, 4, 8]

for s in range(1, len(array)):
    for t in range(s, 0, -1):
        if array[t] < array[t-1]:
            array[t], array[t-1] = array[t-1], array[t]
        else:
            break
print(array)