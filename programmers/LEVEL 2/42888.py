# 오픈채팅방

def solution(record):
    log = {}
    
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            log[i[1]] = i[2]
        
        elif i[0] == "Change":
            log[i[1]] = i[2]
    
    answer = []
    
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            answer.append(f"{log[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(f"{log[i[1]]}님이 나갔습니다.")
    
    return answer


if __name__ == "__main__":
    solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])