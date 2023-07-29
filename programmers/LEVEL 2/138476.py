from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine).most_common()
    answer = 0
    for i in counter:
        if k < 1:
            break
        k -= i[1]
        answer += 1
    return answer