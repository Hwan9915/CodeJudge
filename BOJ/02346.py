# silver
# 풍선 터트리기
import sys
from collections import deque

def main():
    n = int(input())
    deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
    ans = []
    for i in range(n):
        p = deq.popleft()
        ans.append(str(p[0]))
        if p[1] > 0:
            deq.rotate(-(p[1] - 1))
        else:
            deq.rotate(-p[1])
    print(" ".join(ans))

if __name__ == "__main__":
    input = sys.stdin.readline
    main()
