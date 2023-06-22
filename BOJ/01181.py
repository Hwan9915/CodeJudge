# silver 5
# 1181번, 단어 정렬

import sys

N = int(input())
words = sorted(sorted(list({sys.stdin.readline().rstrip() for i in range(N)})), key=lambda x: len(x))


for i in words:
    print(i)
