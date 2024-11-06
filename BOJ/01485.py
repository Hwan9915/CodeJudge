import sys

input = sys.stdin.readline

def cal_len(a, b):
    return ((a[0] - b[0])**2 + (a[1]-b[1])**2)**0.5

def is_square():
    dot = []
    for _ in range(4):
        x, y = map(int, input().rstrip().split())
        dot.append((x, y))
    
    dot.sort()
        
    if cal_len(dot[0],dot[1]) == cal_len(dot[1],dot[3]) == cal_len(dot[0],dot[2]) == cal_len(dot[2], dot[3]):
        if cal_len(dot[0],dot[3]) == cal_len(dot[1], dot[2]):
            return 1 
    return 0
    

def main():
    n = int(input().rstrip())
    for _ in range(n):
        print(is_square())
    

if __name__ == "__main__":
    main()