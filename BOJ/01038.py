# gold
# 감소하는 수

from itertools import combinations

ans = []
comb = list(range(10))

for i in range(1,11):
    for j in combinations(comb,i):
        ans.append(int(''.join(list(map(str,reversed((j)))))))

ans.sort()

n = int(input())

if len(ans) < n+1:
    print(-1)
else:
    print(ans[n])