import sys

input = sys.stdin.readline

def main():
    pos_dict = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8
    }
    move_dict ={
        'R' : [1, 0],
        'L' : [-1, 0],
        'B' : [0, -1],
        'T' : [0, 1],
        'RT' : [1, 1],
        'LT' : [-1, 1],
        'RB' : [1, -1],
        'LB' : [-1, -1]
    }
    k, s, n = list(input().rstrip().split())
    
    k = [pos_dict[k[0]], int(k[1])]
    s = [pos_dict[s[0]], int(s[1])]
    n = int(n)
    
    for i in range(n):
        move = move_dict[input().rstrip()]
        # 킹이 돌 위치로 가는가
        if k[0] + move[0] == s[0] and k[1] + move[1] == s[1]:
            # 돌이 안 나가는가
            if 0 < s[0] + move[0] and s[0] +move[0] < 9 and 0 < s[1] + move[1] and s[1] + move[1] < 9:
                s[0] += move[0]
                s[1] += move[1]
                k[0] += move[0]
                k[1] += move[1]
            else:
                continue
        else:
            if 0 < k[0] + move[0] and k[0] +move[0] < 9 and 0 < k[1] + move[1] and k[1] + move[1] < 9:
                k[0] += move[0]
                k[1] += move[1]
    
    
    print(chr(k[0]+64) + str(k[1]))
    print(chr(s[0]+64) + str(s[1]))
        
        
    
    
if __name__ == "__main__":
    main()