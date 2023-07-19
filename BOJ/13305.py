# silver 3
# 13305번, 주유소
import sys

N = int(sys.stdin.readline().rstrip())

distance = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().strip().split()))

now_price = price[0]
sum_price = now_price * distance[0]
for i in range(1,len(price)-1):
    if now_price > price[i]:
        now_price = price[i]
    sum_price += now_price * distance[i]
print(sum_price)