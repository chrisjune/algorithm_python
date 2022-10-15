char = input()
number_sum = 0
chars = []
for i in char:
    if 'A' <= i <= 'Z':
        chars.append(i)
    else:
        number_sum += int(i)
print(''.join(sorted(chars)) + str(number_sum))
