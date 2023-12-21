# gold
# 크게 만들기
import sys


def main():
    n, k = map(int, input().split())
    cnt = k
    num = list(input().rstrip())

    stack = []
    for i in range(n):
        while cnt > 0 and stack and stack[-1] < num[i]:
            stack.pop()
            cnt -= 1
        stack.append(num[i])

    return ''.join(stack[:n-k])


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())