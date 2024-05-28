def solution(land):
    dp = land
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] += max(dp[i-1][:j]+ dp[i-1][j+1:])
    return max(dp[-1])


if __name__ == "__main__":
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))