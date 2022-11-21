def set_wifi(arr, count, position, start, end):
    mid = (start + end) // 2
    position.append(mid)



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
position = []
set_wifi(sorted(arr), 5, position, 0, len(arr))
print(position)
arr.index()