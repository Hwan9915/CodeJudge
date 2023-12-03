# silver
# 볶음밥 지키기

import sys


def main():
    n, r = map(int, input().rstrip().split())
    rice = []

    for _ in range(n):
        a, b = map(int, input().split())
        rice.append((a, b))

    max_ans = -1
    x, y = -100, -100
    for i in range(-100, 101):
        for j in range(-100, 101):
            ans = 0
            for dot in rice:
                k = ((dot[0] - i) ** 2 + (dot[1] - j)) ** 0.5
                if ((dot[0] - i) ** 2 + (dot[1] - j) ** 2) ** 0.5 <= r:
                    ans += 1
            if ans > max_ans:
                max_ans = ans
                x = i
                y = j

    print(x, y)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
