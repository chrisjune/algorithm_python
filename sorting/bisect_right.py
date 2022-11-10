def bisect_right(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start


print(bisect_right([1, 2, 3, 4, 5], 3, 0, 5))
