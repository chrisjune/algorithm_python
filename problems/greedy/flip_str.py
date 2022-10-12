string = input()

current = string[0]
groups = 1
for s in string[1:]:
    if s == current:
        continue
    groups += 1
    current = s
print(groups // 2)
