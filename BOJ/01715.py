# gold 4
# 1715번, 카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

# 입력
for i in range(N):
    temp = int(input())
    heapq.heappush(heap, temp)

compare_sum = 0

while len(heap) != 1:
    # 최소로 작은 카드 2개를 더해서 합에다가 추가
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    compare_sum += a + b
    # 합친 카드 수를 heap에 저장
    heapq.heappush(heap,a+b)

print(compare_sum)