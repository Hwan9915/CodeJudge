def prime(num:int)->int:
    if num==1:
        return 0
    
    data=[]
    
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            data.append(i)
            if num//i<=10000000:
                return num//i
    if len(data)>=1:
        return data[-1]
    return 1
 
def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(prime(i))
    return answer
