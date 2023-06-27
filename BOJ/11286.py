# silver 1
# 11286번, 절댓값 힙

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    temp = int(input())
    if temp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        # 절댓값이 작은 것들을 출력하기 위해서 abs를 넣음
        # 정렬은 첫번째 값을 기준으로 힙이 만들어짐
        heapq.heappush(heap, (abs(temp), temp))
