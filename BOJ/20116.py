def main():
    n, L = map(int, input().split())
    x = list(map(int, input().split()))
    total_sum = 0 
    total_boxes = 0 
    
    # 아래에서부터 위로 상자를 쌓으면서 확인
    for i in range(n-1, 0, -1):  
        total_sum += x[i] 
        total_boxes += 1 
        
        # 위에 쌓인 상자들의 무게 중심
        avg_x = total_sum / total_boxes
        
        # i번 상자의 구간 안에 무게 중심이 있는지 확인
        if not (x[i-1] - L < avg_x < x[i-1] + L):
            return "unstable"
    
    return "stable"

if __name__ == '__main__':
    print(main())