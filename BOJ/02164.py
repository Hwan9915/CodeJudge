# silver 4
# 2164번, 카드2

from collections import deque

que = deque()

N = int(input())

# queue에 카드 넣기
for i in range(1,N+1):
    que.append(i)

# queue size 가 1 될 때까지 카드를 버리고 옮기기 반복

while len(que) != 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])