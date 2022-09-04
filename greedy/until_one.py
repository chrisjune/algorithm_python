from math import log

if __name__ == "__main__":
    n, k = map(int, input().split())
    total_count = 0
    while n > 1:
        remain = n % k
        if remain == 0:
            n = n // k
        else:
            n = n - 1
        total_count += 1
    print(total_count)
