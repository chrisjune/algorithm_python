if __name__ == '__main__':
    first_line = input()
    second_line = input()

    # m은 최종카운트
    # k는 연속
    numbers_count, max_total_count, max_dup_count = [int(i) for i in first_line.split()]
    numbers = [int(i) for i in second_line.split()]

    numbers.sort()
    first_number_count = max_total_count // (max_dup_count + 1) * max_dup_count + max_total_count % (max_dup_count + 1)
    second_number_count = max_total_count - first_number_count

    print(first_number_count * numbers[-1] + second_number_count * numbers[-2])
