def merge_two_arr(left, right):
    leftidx = 0
    rightidx = 0
    result = []

    while leftidx < len(left) and rightidx < len(right):
        if left[leftidx] < right[rightidx]:
            result.append(left[leftidx])
            leftidx += 1
        else:
            result.append(right[rightidx])
            rightidx += 1
    # 3 4 x 10
    if leftidx >= len(left):
        targetidx = rightidx
        targetarr = right
    else:
        targetidx = leftidx
        targetarr = left

    result.extend(targetarr[targetidx:])
    return result


left_arr = [1, 3, 8]
right_arr = [2, 6, 7, 7.5, 10, 11, 12]
print(merge_two_arr(left_arr, right_arr))
