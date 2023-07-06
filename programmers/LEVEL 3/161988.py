def solution(sequence):
    sequence_parse = [sequence[i] * (1 if i % 2 == 0 else -1) for i in range(len(sequence))]
    dp = [[0, 0] for _ in range(len(sequence))]
    dp[0][0] = sequence_parse[0]
    dp[0][1] = sequence_parse[0]
    for i in range(1, len(sequence_parse)):
        # 수열에 대해 각각 최소값과 최대값 저장
        dp[i][0] = min(sequence_parse[i], sequence_parse[i] + dp[i - 1][0])
        dp[i][1] = max(sequence_parse[i], sequence_parse[i] + dp[i - 1][1])

    # 배열 안 가장 작은 수와 가장 큰 수를 탐색
    val_min = min(map(min,dp))
    val_max = max(map(max,dp))

    # 절대값이 가장 큰 수 반환
    return max(abs(val_min),abs(val_max))