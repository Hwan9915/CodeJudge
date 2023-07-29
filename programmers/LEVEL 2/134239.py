def solution(k, ranges):
    k_list = [k]
    while k != 1:
        if k % 2 == 0:
            k = k// 2
            k_list.append(k)
        else:
            k = k * 3 + 1
            k_list.append(k)

    integral = []
    for i in range(len(k_list)-1):
        temp = (k_list[i]+k_list[i+1])/2
        integral.append(temp)

    answer = []
    for i in ranges:
        a,b = i[0], len(k_list)+i[1]-1
        if b < a:
            answer.append(-1.0)
        else:
            answer.append(float(sum(integral[a:b])))
    return answer