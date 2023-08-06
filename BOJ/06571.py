# silver
# 피보나치 수 개수
import sys

fibo = [0,1,2]
while fibo[-1] < 10**100:
    fibo.append(fibo[-1] + fibo[-2])


while True:
    answer = 0
    a, b = map(int, input().rstrip().split())
    if a == 0 and b == 0:
        break
    for i in range(1,len(fibo)):
        if a <= fibo[i] <= b:
            answer += 1
    print(answer)

