# gold
# 동전 1
import sys

def main():
    n, k = map(int, input().rstrip().split())
    coins = [int(input()) for i in range(n)]

    dp = [0 for i in range(k+1)]

    dp[0] = 1
    for coin in coins:
        for j in range(1, k+1):
            if j-coin >= 0:
                dp[j] = dp[j] + dp[j-coin]

    return dp[-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())