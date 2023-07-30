# silver
# 18230번, 2xN 예쁜 타일링
import sys,collections

input = sys.stdin.readline

n, a, b = map(int, input().rstrip().split())
a_list = collections.deque(sorted(list(map(int, input().rstrip().split()))))
b_list = collections.deque(sorted(list(map(int, input().rstrip().split()))))

ans = 0
if n % 2 == 1:
    ans += a_list.pop()
    n -= 1

while n != 0:
    a, b = 0, 0
    if len(a_list) > 1:
        a = a_list[-1] + a_list[-2]
    if len(b_list) > 0:
        b = b_list[-1]

    if a > b:
        a_list.pop()
        a_list.pop()
        ans += a
    else:
        b_list.pop()
        ans += b
    n-= 2

print(ans)