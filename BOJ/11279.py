# silver 2
# 11279번, 최대 힙

import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    temp = int(input())
    if temp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap, -temp)

