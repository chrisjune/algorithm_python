from bisect import bisect_left, bisect_right

arr = [1, 1, 2, 2, 2, 2, 4]

result = bisect_right(arr, 6) - bisect_left(arr, 6)
if not result:
    print(-1)
else:
    print(result)
