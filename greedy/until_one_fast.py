if __name__ == '__main__':
    n, k = map(int, input().split())
    count = 0
    while True:
        remain = n % k
        n = n - remain
        count += remain
        n = n // k
        count += 1

        if n < k:
            break

    count += n-1
    print(count)
