# silver
# 25496번, 장신구 명장 임스
import sys

input = sys.stdin.readline

p, n = map(int , input().rstrip().split())
a_list = sorted(list(map(int, input().rstrip().split())))
ans = 0
for i in a_list:
    if p < 200:
        p += i
        ans += 1
    else:
        break

print(ans)