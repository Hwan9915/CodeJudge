import math

def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        temp =math.isqrt(pow(d, 2) - pow(i, 2))
        answer += temp//k + 1
    return answer

print(solution(1,5))