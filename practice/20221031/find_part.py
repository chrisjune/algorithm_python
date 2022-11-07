n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
targets = list(map(int, input().split()))

from bisect import bisect_left


def binary_search(arr, t, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == t:
            return mid

        if arr[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    return None


result = []
for target in targets:
    if binary_search(parts, target, 0, len(parts) - 1):
        result.append(True)
    else:
        result.append(False)
print(result)
