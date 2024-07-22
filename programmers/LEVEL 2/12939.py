def solution(s):
    a= list(map(int,s.split()))
    return str(min(a)) +" "+str(max(a))

if __name__ == "__main__":
    print(solution("1 2 3 4"))