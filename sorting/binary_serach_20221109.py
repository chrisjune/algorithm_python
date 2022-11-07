def binary_search(arrays, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arrays[mid] == target:
            return mid

        if arrays[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return None

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 0, 9))
