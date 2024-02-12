# gold
# AC
import sys

from collections import deque

def main():
    for __ in range(int(input().rstrip())):
        commands = list(input().rstrip())
        n = int(input())
        tmp = input().rstrip()
        # 배열 입력
        if tmp == '[]':
            lst = deque([])
        else:
            lst = deque(list(tmp[1:-1].split(',')))

        reverse = False
        for command in commands:
            if command == 'R':
                if reverse:
                    reverse = False
                else:
                    reverse = True
            elif command == 'D':
                if len(lst) == 0:
                    print('error')
                    break
                elif reverse:
                    lst.pop()
                else:
                    lst.popleft()
        else:
            if len(lst) == 0:
                print("[]")
            elif reverse:
                print("[" + ",".join(list(lst)[::-1]) + "]")
            else:
                print("[" + ",".join(list(lst)) + "]")


if __name__ == "__main__":
    input = sys.stdin.readline
    main()