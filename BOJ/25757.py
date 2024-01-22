# silver
# 임스와 함께하는 미니게임
import sys


def main():
    global need_p
    n, game = input().rstrip().split()
    n = int(n)
    if game == "Y":
        need_p = 2
    elif game == "F":
        need_p = 3
    elif game == "O":
        need_p = 4

    player = set()
    for i in range(n):
        tmp = input().rstrip()
        player.add(tmp)

    return len(list(player)) // (need_p - 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())
