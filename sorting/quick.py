array = [5, 7, 9, 0, 3, 1, 6, 2, 4]


def quick(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈린경우
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않은 경우
        else:
            array[left], array[right] = array[right], array[left]
        print(array)
    quick(array, right+1, end)
    quick(array, start, right-1)


quick(array, 0, len(array) - 1)
