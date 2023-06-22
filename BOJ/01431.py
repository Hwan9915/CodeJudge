# silver 3
# 1431번, 시리얼 번호

import sys

N = int(input())
serial_temp = [sys.stdin.readline().rstrip() for i in range(N)]
serials = []
for serial in serial_temp:
    # 단어의 숫자들의 합을 구하는 변수
    temp_sum = 0
    for i in serial:
        # 숫자인 경우
        if i.isdigit():
            temp_sum = temp_sum + int(i)
    serials.append((serial, len(serial), temp_sum))


# 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.


# 1,2,3 번 순으로 serials를 정렬
serials = sorted(serials, key=lambda x: (x[1], x[2], x[0]))
for i in serials:
    print(i[0])
