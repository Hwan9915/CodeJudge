import sys

input = sys.stdin.readline
mx = -10e9
mn =  10e9
  
def dfs(num_lst, operator_lst, index, current_value):
    global mx, mn
    if index == len(num_lst):
        mx = max(mx, current_value)
        mn = min(mn, current_value) 
        return
    
    if operator_lst[0] > 0:
        operator_lst[0] -= 1
        dfs(num_lst, operator_lst, index+1, current_value + num_lst[index])
        operator_lst[0] += 1
    
    if operator_lst[1] > 0:
        operator_lst[1] -= 1
        dfs(num_lst, operator_lst, index+1, current_value - num_lst[index])
        operator_lst[1] += 1
    
    if operator_lst[2] > 0:
        operator_lst[2] -= 1
        dfs(num_lst, operator_lst, index+1, current_value * num_lst[index])
        operator_lst[2] += 1
    
    if operator_lst[3] > 0:
        operator_lst[3] -= 1
        if current_value < 0:
            dfs(num_lst, operator_lst, index + 1, -(-current_value // num_lst[index]))
        else:
            dfs(num_lst, operator_lst, index + 1, current_value // num_lst[index])
        operator_lst[3] += 1


def main():
    n = int(input().rstrip())
    num_lst = list(map(int, input().rstrip().split()))
    operator_lst = list(map(int, input().rstrip().split()))

    dfs(num_lst, operator_lst, 1, num_lst[0])
    print(mx)
    print(mn)

if __name__ == "__main__":
    main()