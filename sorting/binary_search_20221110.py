def binary_search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        print(start, end, mid)
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end

