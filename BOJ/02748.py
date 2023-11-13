# bronze
# 피보나치 수 2
import sys
input = sys.stdin.readline

# 피보나치 배열 초기값
fibo = [0,1,1]

# n 값 입력
n = int(input())


# n까지 피보나치 배열 메모이제이션
for i in range(2,n):
    fibo.append(fibo[-1]+fibo[-2])

print(fibo[n])
