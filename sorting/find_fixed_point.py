def bisect(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return bisect(arr, start, mid - 1)
    else:
        return bisect(arr, mid + 1, end)


# n = int(input())
# arr = list(map(int, input().split()))
arr = [-15, 0, 1, 3, 4]
print(bisect(arr, 0, len(arr)))
