# silver
# 빈도 정렬

message = dict()

N, C = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if not i in message:
        message[i] = 1
    else:
        message[i] += 1
num_list = []

for i in message:
    num_list.append([i, message[i]])

num_list.sort(key=lambda x: -x[1])
for i in num_list:
    for j in range(i[1]):
        print(i[0], end=' ')