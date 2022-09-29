array = [7, 5, 0, 3, 1, 6, 2, 4, 8]

for s in range(len(array)):
    m = s
    for t in range(s, len(array)):
        if array[m] > array[t]:
            m = t
    array[m], array[s] = array[s], array[m]

print(array)

