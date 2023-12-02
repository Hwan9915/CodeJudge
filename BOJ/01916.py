# gold
# 최소비용 구하기
import sys
from heapq import heappop, heappush

def main():
    INF = 10e8
    vertex = int(input())
    edge = int(input())

    dp = [INF] * (vertex + 1)
    graph = [[] for _ in range(vertex + 1)]

    for _ in range(edge):
        u, v, w = map(int, input().rstrip().split())
        graph[u].append((w,v))

    def dijkstra(start,end):
        min_heap = []
        dp[start] = 0
        heappush(min_heap,(0, start))
        while min_heap:
            sum_wei, now_node = heappop(min_heap)

            if dp[now_node] < sum_wei:
                continue

            for now_wei, next_node in graph[now_node]:
                next_wei = now_wei + sum_wei
                if dp[next_node] > next_wei:
                    dp[next_node] = next_wei
                    heappush(min_heap,(next_wei,next_node))
        return dp[end]
    start, end = map(int, input().split())

    return dijkstra(start,end)


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())