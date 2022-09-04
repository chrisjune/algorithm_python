from math import inf

if __name__ == '__main__':
    row, col = map(int, input().split())
    max_value = -inf
    for _ in range(row):
        numbers = list(map(int, input().split()))
        max_value = max(max_value, min(numbers))
    print(max_value)
