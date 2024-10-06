
import sys

input = sys.stdin.readline

def main():
    ans = 0
    query_dict = dict()
    n = int(input().rstrip())
    for _ in range(n):
        query = list(input().rstrip().split())
        if query[0] == '1':
            inform_lst = list(map(int,query[3:]))
            if query[1] in query_dict:
                tmp_lst = query_dict[query[1]] + inform_lst
                tmp_lst.sort(reverse=True)
                query_dict[query[1]] = tmp_lst
            else:
                inform_lst.sort(reverse=True)
                query_dict[query[1]] = inform_lst
        else:
            if query[1] in query_dict:
                if int(query[2]) >= len(query_dict[query[1]]):
                    ans += sum(query_dict[query[1]])
                    query_dict.pop(query[1])
                else:
                    for __ in range(int(query[2])):
                        ans += query_dict[query[1]].pop(0)
    return ans

if __name__ == "__main__":
    print(main())