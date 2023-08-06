def solution(elements):

    elements_sum = set()
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            a = j
            b = j + i
            if b > len(elements):
                temp1 = sum(elements[a:len(elements)])
                temp2 = sum(elements[0:b - len(elements)])
                elements_sum.add(temp1+temp2)
            else:
                elements_sum.add(sum(elements[a:b]))

    return len(elements_sum)