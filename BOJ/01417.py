# silver
# 국회의원 선거
import sys, heapq


def main():
    n = int(input())
    if n == 1:
        return 0

    max_heap = []
    ans = 0

    dasom = int(input().rstrip())
    for _ in range(n-1):
        tmp = int(input().rstrip())
        heapq.heappush(max_heap,(-tmp))

    while True:
        tmp = -heapq.heappop(max_heap)
        if dasom > tmp:
            return ans
        tmp -= 1
        ans += 1
        dasom += 1
        heapq.heappush(max_heap,(-tmp))

if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())