from collections import Counter

def solution(want, number, discount):
    answer = 0
    user = dict()
    for i in zip(want,number):
        user[i[0]] = i[1]

    for i in range(0,len(discount)-sum(number)+1):
        mart = Counter(discount[i:i+10])
        user_counter = Counter(user)
        if user_counter == mart:
            answer += 1
    return answer