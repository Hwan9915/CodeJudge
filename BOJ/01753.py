# gold
# 최단경로

import sys
import heapq


def main():
    INF = sys.maxsize

    vertex, edge = map(int, input().split())
    k = int(input())

    graph = [[] for _ in range(vertex + 1)]
    dp = [INF for _ in range(vertex + 1)]
    min_heap = []

    for _ in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))

    def dijkstra(start):
        dp[start] = 0
        heapq.heappush(min_heap, (0, start))
        while min_heap:
            sum_wei, now_node = heapq.heappop(min_heap)

            if dp[now_node] < sum_wei:
                continue

            for now_wei, next_node in graph[now_node]:
                next_wei = sum_wei + now_wei
                if dp[next_node] > next_wei:
                    dp[next_node] = next_wei
                    heapq.heappush(min_heap, (next_wei, next_node))

    dijkstra(k)

    for i in range(1, vertex + 1):
        if dp[i] == INF:
            print('INF\n')
        else:
            print('%d\n'%dp[i])


if __name__ == "__main__":
    input = sys.stdin.readline
    print = sys.stdout.write
    main()
