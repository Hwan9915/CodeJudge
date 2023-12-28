# gold
# 과제
import sys
import heapq

def main():
    n = int(input().rstrip())
    lst = [list(map(int, input().rstrip().split())) for _ in range(n)]
    lst.sort()

    # idx[0]이 같거나 큰 수 중에 idx[1]이 가장 큰 수를 더한다.∂
    min_heap = []
    t = lst[-1][0]

    ans = 0

    for i in range(t, 0, -1):

        while lst and lst[-1][0] >= i:
            heapq.heappush(min_heap,-lst.pop()[1])

        if len(min_heap) > 0:
            ans += -heapq.heappop(min_heap)

    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
