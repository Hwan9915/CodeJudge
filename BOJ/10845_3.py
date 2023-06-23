# silver 4
# 10845번, 큐
# collection.deque 사용

import sys, collections

N = int(input())
que = collections.deque()

for i in range(N):
    # 명령어 입력
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push':
        que.appendleft(cmd[1])
    elif cmd[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop())
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif cmd[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
