# silver
# 에디터
import sys


def main():
    first = list(input().rstrip())
    second = []
    for __ in range(int(input())):
        command = list(input().rstrip().split())
        if command[0] == 'L':
            if first:
                second.append(first.pop(-1))
        elif command[0] == 'D':
            if second:
                first.append(second.pop(-1))
        elif command[0] == 'P':
            first.append(command[1])
        else:
            if first:
                first.pop(-1)
    second.reverse()
    print(''.join(first+second))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()