# silver 4
# 15828번, Router

import collections
import sys

input = sys.stdin.readline
deq = collections.deque()

# Queue size 입력
N = int(input())

while True:
    temp = int(input())
    # -1 인 경우, 종료
    if temp == -1:
        break
    # 0 인 경우, popleft
    elif temp == 0:
        deq.popleft()
    else:
        # queue size 보다 작게 찬 경우 append
        if len(deq) < N:
            deq.append(temp)
        # 그 외의 경우는 continue
        else:
            continue

if len(deq) == 0:
    print("empty")
else:
    for i in deq:
        print(i, "", end="")
