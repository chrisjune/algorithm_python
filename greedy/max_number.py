if __name__ == '__main__':
    first_line = input()
    second_line = input()

    # m은 최종카운트
    # k는 연속
    numbers_count, max_total_count, max_dup_count = [int(i) for i in first_line.split()]
    numbers = [int(i) for i in second_line.split()]

    print(numbers_count, max_total_count, max_dup_count, numbers)
    numbers.sort()
    total_count = 0
    max_number_count = 0
    total_sum = 0
    while total_count < max_total_count:
        if max_number_count < max_dup_count:
            total_sum += numbers[-1]
            max_number_count += 1
        else:
            total_sum += numbers[-2]
            max_number_count = 0

        total_count += 1
    print(total_sum)
