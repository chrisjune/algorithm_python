import bisect
import collections
import heapq
from itertools import permutations, combinations, combinations_with_replacement, product
import math

if __name__ == '__main__':
    target = ['a', 'b', 'c']
    # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    print(list(permutations(target)))
    # 6
    print(len(list(permutations(target))))

    # [('a', 'b', 'c')]
    print(list(combinations(target, 3)))
    # [('a', 'b'), ('a', 'c'), ('b', 'c')]
    print(list(combinations(target, 2)))
    # 3
    print(len(list(combinations(target, 2))))

    # [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')]
    print(list(combinations_with_replacement(target, 3)))
    # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
    print(list(combinations_with_replacement(target, 2)))
    # [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
    print(list(product(target, repeat=2)))

    # heapq
    number_list = [1, 8, 3, 6, 2, 9, 5, 4]
    heap_list = []
    for i in number_list:
        heapq.heappush(heap_list, i)
    # [1, 2, 3, 4, 6, 9, 5, 8]
    print(heap_list)

    for _ in range(len(number_list)):
        print(heapq.heappop(heap_list))
        print(heap_list)

    # [1, 2, 3, 4, 6, 9, 5, 8]
    heapq.heapify(number_list)
    print(number_list)

    # bisect
    ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 3
    print(bisect.bisect_left(ordered_list, 4))
    # 4
    print(bisect.bisect_right(ordered_list, 4))
    # 5 // 2 * log(n)
    dup_ordered_list = [1, 1, 2, 2, 2, 4, 4, 4, 4, 4, 5, 6, 7]
    print(bisect.bisect_right(dup_ordered_list, 4) - bisect.bisect_left(dup_ordered_list, 4))

    # deque
    # queue
    queue_list = [1, 2, 3, 4, 5]
    queue = collections.deque(queue_list)
    # [1, 2, 3, 4, 5]
    print(list(queue))
    queue.popleft()
    # [2, 3, 4, 5]
    print(list(queue))
    queue.append(6)
    # [2, 3, 4, 5, 6]
    print(list(queue))

    # stack
    stack_list = [1, 2, 3]
    stack = collections.deque(stack_list)
    # [1, 2, 3]
    print(list(stack))
    stack.pop()
    # [1, 2]
    print(list(stack))
    stack.append(4)
    # [1, 2, 4]
    print(list(stack))

    # Counter({'A': 2, 'B': 2, 'BB': 2, 'AB': 1, 'AA': 1})
    words = 'A B AB BB AA BB A B'.split()
    print(collections.Counter(words))

    # 7
    print(math.gcd(21, 14))
    # 42
    print(21 * 14 / math.gcd(21, 14))
