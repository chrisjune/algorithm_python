build_frames = [
    [1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]
]


def possible(answer):
    for ans in answer:
        x, y, kind = ans
        # 기둥
        if kind == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
        if kind == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
        return False
    return True


answer = []
for frame in build_frames:
    x, y, kind, command = frame
    ans = [x, y, kind]
    # 삭제시
    if command == 0:
        answer.remove(ans)
        if not possible(answer):
            answer.append(ans)
    if command == 1:
        answer.append(ans)
        if not possible(answer):
            answer.remove(ans)
print(sorted(answer))
