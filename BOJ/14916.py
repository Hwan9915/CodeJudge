# silver
# 거스름돈
import sys
input = sys.stdin.readline

# 입력
n = int(input())

# 불가능한 경우
if n == 1 or n == 3:
    print(-1)
    exit(0)


# 초기 동전 값 계산
coin5 = n // 5
coin2 = (n - coin5 * 5) // 2

# 나머지 값 계산
m = n - (coin5 * 5 + coin2 * 2)

# 나머지가 0인 경우 코인의 합 출력
while m != 0:
    coin5 -= 1
    m += 5
    coin2 += m // 2
    m = m % 2

print(coin5 + coin2)