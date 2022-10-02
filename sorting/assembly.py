def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


n = input()
targets = list(map(int, input().split()))

m = input()
sources = list(map(int, input().split()))

targets.sort()

for source in sources:
    if binary_search(targets, source, 0, len(targets) - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
