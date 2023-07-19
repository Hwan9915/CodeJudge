# silver 3
# 9440번, 숫자 더하기
import sys
from collections import deque

while True:
    arr = deque(map(int, sys.stdin.readline().rstrip().split()))
    if arr[0] == 0:
        break
    arr.popleft()
    # 정렬
    arr = sorted(arr)
    zeros = 0
    # 0의 갯수 세기
    for i in arr:
        if i == 0:
            zeros += 1
        else:
            break
    # 0을 index 2번째 위치에 모두 넣기
    for i in range(zeros):
        arr.pop(0)
    for i in range(zeros):
        arr.insert(2,0)

    a, b = [], []
    # 짝수인 경우
    if len(arr)% 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                a.append(arr[i])
            else:
                b.append(arr[i])
        print(int("".join(map(str,a)))+ int("".join(map(str,b))))
    # 홀수인 경우
    else:
        a.append(arr[0])
        for i in range(1,len(arr)):
            if i % 2 == 1:
                a.append(arr[i])
            else:
                b.append(arr[i])
        print(int("".join(map(str,a)))+ int("".join(map(str,b))))

