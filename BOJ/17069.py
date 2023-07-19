# gold 4
# 17059번, 파이프 옮기기 2
import sys

# 입력
N = int(input())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 대각선, 세로, 가로
dp = [[[0] * 3 for _ in range(N + 1)] for __ in range(N + 1)]
dp[1][2][2] = 1
for i in range(1, N + 1):
    for j in range(3, N + 1):
        if matrix[i - 1][j - 1] == 0:
            # 대각선
            if matrix[i - 1][j - 2] == 0 and matrix[i - 2][j - 1] == 0:
                dp[i][j][0] = sum(dp[i - 1][j - 1])
            dp[i][j][1] = dp[i - 1][j][0] + dp[i - 1][j][1]
            dp[i][j][2] = dp[i][j - 1][0] + dp[i][j - 1][2]

print(sum(dp[N][N]))