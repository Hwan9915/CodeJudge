# gold
# 감소하는 수

from itertools import combinations

ans = []
comb = list(range(10))

for i in range(1,11):
    for j in combinations(comb,i):
        ans.append(int(''.join(list(map(str,reversed((j)))))))

# 10 C 10  0,1,2,3,4,5,6,7,8,9 9876543210
ans.sort()

n = int(input())

if len(ans) < n+1:
    print(-1)
else:
    print(ans[n])