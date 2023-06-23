# silver 4
# 1158번, 요세푸스 문제

import sys, collections

N, K = map(int, sys.stdin.readline().rstrip().split())

# 큐 생성
deq = collections.deque()

# 순열 만들기
for i in range(1, N + 1):
    deq.append(i)

# 정답을 넣을 리스트
ans = []

# K-1 번 회전하고 K번째에서 맨 앞의 요소를 제거후 ans에 넣는다.
while len(deq) != 0:
    deq.rotate(-(K - 1))
    ans.append(deq.popleft())

# 출력
print('<', end="")
for i in range(len(ans) - 1):
    print(ans[i],', ', sep="", end="")
print(ans[-1],'>', sep="")
