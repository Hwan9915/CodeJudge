# silver 2
# 1927번, 최소 힙

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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, temp)

