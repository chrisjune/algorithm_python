from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    # 0에서 weak을 시작점으로
    for start in range(length):
        [7, 3, 4]
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                # 점검할 수 있는 범위를 넘어설 경우
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
