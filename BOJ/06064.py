import sys

input = sys.stdin.readline

def num_6064(m, n, x, y):
    m_big = True
    if n > m:
        m_big = False
    
    if m_big:
        # 초기 깂 설정
        k = x; a = x
        b = m % n if m % n != 0 else 1
        while k < m*n:
            k += m
            b += m
            b = b % m if b % m != 0 else 1
            if a == x and b == y:
                return k
    else:
        k = y
        
        a = y % m if y % m != 0 else 1
        b = y
        while k < m*n:
            k += n
            a += n
            a = a % m if a % m != 0 else 1
            if a == x and b == y:
                return k
        
    return -1
    

def main():
    t = int(input().rstrip())
    
    for _ in range(t):
        m, n, x, y = map(int,input().rstrip().split())
        print(num_6064(m,n,x,y))
        
    
    
if __name__ == "__main__":
    main()