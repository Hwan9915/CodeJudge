import itertools

def check(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]):
            return False

        for j in range(len(user[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(itertools.permutations(user_id, len(banned_id)))
    ban_set = []
    
    for user in user_permutation:
        if not check(user, banned_id):
            continue
        else:
            user = set(user)
            if user not in ban_set:
                ban_set.append(user)
    
    
    return len(ban_set)
            



if __name__ == "__main__":
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
                   ["fr*d*", "*rodo", "******", "******"]))