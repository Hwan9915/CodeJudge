# silver 4
# 10845번, 큐
# 오류이유: queue 클래스는 index를 지원하지 않는다.

import queue, sys
N = int(input())
que = queue.Queue()

for i in range(N):
    # 명령어 입력
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push':
        que.put(cmd[1])
    elif cmd[0] == 'pop':
        if not que.empty():
            print(que.get())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(que.qsize())
    elif cmd[0] == 'empty':
        if que.empty():
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if que.empty():
            print(-1)
        else:
            # 인덱스 오류 발생
            print(que[que.qsize()-1])
    elif cmd[0] == 'back':
        if que.empty():
            print(-1)
        else:
            # 인덱스 오류 발생
            print(que[0])
