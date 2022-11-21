def binary_search(arr, t, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < t:
            start = mid + 1
        else:
            end = mid
    return start


arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr, 1, 0, len(arr)))
