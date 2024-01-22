# silver
# 쿠키의 신체 측정
import sys


def main():
    n = int(input().rstrip())
    lst = [list(input().rstrip()) for i in range(n)]
    heart = []
    find = False

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if lst[i][j + 1] == "*" and lst[i][j - 1] == "*" and lst[i - 1][j] == "*" and lst[i + 1][j] == "*":
                heart.append((i, j))
                find = True
            if find:
                break
        if find:
            break

    k, l = heart[0]

    # left arm
    left_arm = 0
    for i in range(l - 1, -1, -1):
        if lst[k][i] == '*':
            left_arm += 1
        else:
            break

    # right arm
    right_arm = 0
    for i in range(l + 1, n):
        if lst[k][i] == '*':
            right_arm += 1
        else:
            break

    # back
    back = 0
    for i in range(k + 1, n):
        if lst[i][l] == '*':
            back += 1
        else:
            heart.append((i,l))
            break

    k, l = heart[1]

    # left leg
    left_leg = 0
    for i in range(k, n):
        if lst[i][l-1] == '*':
            left_leg += 1
        else:
            break

    # right leg
    right_leg = 0
    for i in range(k, n):
        if lst[i][l+1] == '*':
            right_leg += 1
        else:
            break

    print(heart[0][0]+1, heart[0][1]+1)
    print(left_arm, right_arm, back, left_leg, right_leg)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
