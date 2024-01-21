# bronze
# ZOAC 4
import sys

def main():
    h, w, n, m = map(int, input().strip().split())
    l = h // (n + 1)
    if h % (n+1) != 0:
        l += 1

    k = w // (m + 1)
    if w % (m + 1) != 0:
        k += 1
    return l * k


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())