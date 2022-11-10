def bisect_left(arr, target, start, end):
    while start < end:
        mid = (start+end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


print(bisect_left([1, 2, 3, 4, 5], 2.5, 0, 5))
