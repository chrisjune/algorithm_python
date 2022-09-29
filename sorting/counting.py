array = [5, 7, 9, 0, 3, 1, 6, 2, 4]


def counting(array):
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1

    for idx, i in enumerate(count):
        for j in range(i):
            print(idx, end=' ')

counting(array)