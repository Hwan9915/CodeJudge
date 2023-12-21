# gold
# 집 구하기
import sys
from heapq import heappush, heappop

def main():
    # 정보 입력
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a].append((b,w))
        graph[b].append((a,w))

    mac_n, mac_dis = map(int, input().split())
    mac_list = list(map(int, input().split()))

    star_n, star_dis = map(int, input().split())
    star_list = list(map(int, input().split()))

    # 스타벅스, 맥도날드 아닌 정점 리스트 만들기
    house = list(range(1,v+1))
    for i in mac_list:
        house.remove(i)
    for i in star_list:
        house.remove(i)

    def dijkstra(start):
        dp = [INF] * (v + 1)
        dp[start] = 0
        min_heap = []
        heappush(min_heap,(0,start))
        while min_heap:
            sum_wei, now_node = heappop(min_heap)
            if dp[now_node] < sum_wei:
                continue
            for next_node, now_wei in graph[now_node]:
                next_wei = sum_wei + now_wei
                if dp[next_node] > next_wei:
                    dp[next_node] = next_wei
                    heappush(min_heap,(next_wei, next_node))
        return dp

    ans = INF
    for k in house:
        lst = dijkstra(k)
        is_star = False
        is_mac = False

        star_min = INF
        mac_min = INF

        for star in star_list:
            if lst[star] <= star_dis:
                is_star = True
                if star_min > lst[star]:
                    star_min = lst[star]

        for mac in mac_list:
            if lst[mac] <= mac_dis:
                is_mac = True
                if mac_min > lst[mac]:
                    mac_min = lst[mac]
        if is_mac and is_star:
            if ans > mac_min + star_min:
                ans = mac_min + star_min

    return ans if ans != INF else -1



if __name__ == "__main__":
    input = sys.stdin.readline
    INF = sys.maxsize
    print(main())