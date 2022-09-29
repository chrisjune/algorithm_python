array = [5, 7, 9, 0, 3, 1, 6, 2, 4]


def quick(array):
    if len(array) <= 1: return array
    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i <= pivot]
    right_side = [i for i in tail if i > pivot]
    return quick(left_side) + [pivot] + quick(right_side)


print(quick(array))
