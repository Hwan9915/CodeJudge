# silver
# 숫자놀이

import sys

def main():
    num = ['zero ', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
    num_dict = {'zero': '0','one':'1', 'two':'2','three':'3' , 'four':'4', 'five' : '5', 'six' : '6', 'seven': '7', 'eight' : '8', 'nine' : '9'}
    arr = []
    n, m = map(int, input().rstrip().split())
    for i in range(n,m+1):
        i_lst = list(str(i))
        i_str = ""
        for j in range(len(i_lst)):
            i_str += num[int(i_lst[j])]
        arr.append(i_str)
    arr.sort()

    for i in range(len(arr)):
        a = arr[i].split()
        tmp = ''
        for k in a:
            tmp += num_dict[k]
        print(tmp+" ",end='')
        if i % 10 == 9:
            print()


if __name__ == '__main__':
    main()