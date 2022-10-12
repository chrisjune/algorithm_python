data = [int(i) for i in input()]
total = data[0]
if len(data) > 1:
    for d in data[1:]:
        if total <= 1 or d <= 1:
            total = total + d
        else:
            total = total * d
print(total)
