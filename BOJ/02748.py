# bronze
# 피보나치 수 2
import sys
input = sys.stdin.readline

fibo = [0,1,1]
n = int(input())

for i in range(2,n):
    fibo.append(fibo[-1]+fibo[-2])

print(fibo[n])
