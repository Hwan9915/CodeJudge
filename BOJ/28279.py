# silver
# 덱 2
from collections import deque

import sys


def main():
    n = int(input().rstrip())
    deq = deque()
    for __ in range(n):
        command = input().rstrip()
        if command[0] == '1' or command[0] == '2':
            if command[0] == '1':
                deq.appendleft(int(command[2:]))
            elif command[0] == '2':
                deq.append(int(command[2:]))
        # 3 ~ 8
        elif command[0] == '3':
            print(deq.popleft() if len(deq) != 0 else -1)
        elif command[0] == '4':
            print(deq.pop() if len(deq) != 0 else -1)
        elif command[0] == '5':
            print(len(deq))
        elif command[0] == '6':
            print(1 if len(deq) == 0 else 0)
        elif command[0] == '7':
            print(deq[0] if len(deq) != 0 else -1)
        elif command[0] == '8':
            print(deq[-1] if len(deq) != 0 else -1)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()