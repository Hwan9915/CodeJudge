# Bronze 2
# 2750번, 수 정렬하기

N = int(input())
num_list = []
for i in range(N):
    temp = int(input())
    num_list.append(temp)

num_list.sort()

for i in num_list:
    print(i)

