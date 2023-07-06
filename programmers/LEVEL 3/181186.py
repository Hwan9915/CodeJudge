def solution(n):
    dp = [0 for _ in range(100001)]
    sum_dp = [0 for _ in range(100001)]

    sum_dp[1] = 1
    sum_dp[2] = 3
    sum_dp[3] = 11
    sum_dp[4] = 24
    sum_dp[5] = 65
    sum_dp[6] = 181

    dp[1] = 1
    dp[2] = 3
    dp[3] = 10
    dp[4] = 23
    dp[5] = 62
    dp[6] = 170

    for i in range(7, n+1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2 + dp[i - 3] * 5 + sum_dp[i - 4] * 2 + sum_dp[i - 5] * 2 + sum_dp[i - 6] * 4
        dp[i] = dp[i] % 1000000007

        sum_dp[i] = dp[i] + sum_dp[i-3]
        sum_dp[i] = sum_dp[i] % 1000000007
    return dp[n]