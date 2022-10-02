inputs = int(input())
input_list = []
for _ in range(inputs):
    input_list.append(int(input()))
    input_list.sort(reverse=True)

for i in input_list:
    print(i, end=' ' )
