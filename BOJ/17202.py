import sys
input = sys.stdin.readline

# 입력
a = input().rstrip()
b = input().rstrip()

# 정답을 저장할 배열
ans = []

# 초기 배열 입력
for i in range(len(a)):
    ans.append(int(a[i]))
    ans.append(int(b[i]))

# 배열의 길이가 2인 경우 출력
while len(ans) > 2:
    # 배열에 대해 계산
    for i in range(len(ans)-1):
        # 더한 값을 10으로 나머지 계산을 통해 값 계산
        ans[i] = (ans[i] + ans[i+1]) % 10
    # 마지막 배열 삭제
    ans.pop()

# 배열 출력
print(''.join(map(str,ans)))