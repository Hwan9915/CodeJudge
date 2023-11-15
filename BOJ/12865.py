import sys
input = sys.stdin.readline

# N과 K 입력
N, K = map(int, input().split())

# 저장할 배열 초기화
cache = [0] * (K + 1)

for _ in range(N):
    # 과자 무게, 과자 가치
    w, v = map(int, input().split())

    # 가방 최대로 넣는 계산
    for i in range(K, w - 1, -1):
        cache[i] = max(cache[i], v + cache[i - w])


print(cache[-1])