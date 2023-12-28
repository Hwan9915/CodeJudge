# gold
# 강의실
import sys
import heapq


def main():
    n = int(input())
    lst = [tuple(map(int, input().rstrip().split()))[1:] for _ in range(n)]
    lst.sort()
    min_heap = [lst[0][1]]

    for study in lst[1:]:
        if min_heap[0] > study[0]:
            heapq.heappush(min_heap,(study[1]))
        else:
            heapq.heappushpop(min_heap,(study[1]))


    return len(min_heap)



if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())