import sys
n, target = map(int, input().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(height)
def binary(height, target, start, end):
    while start <=end:
        mid = (start + end) // 2

        length = 0
        for h in height:
            if h > mid:
                length += h-mid

        if length == target:
            return mid
        elif length < target:
            end = mid -1
        else:
            start = mid + 1
    return None

print(binary(height, target, start, end))