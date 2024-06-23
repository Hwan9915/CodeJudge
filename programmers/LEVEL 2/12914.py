def solution(n):
    a = [0 for _ in range(2001)]
    a[1], a[2] = 1, 2
    for i in range(3,n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n] % 1234567


if __name__ == "__main__":
    print(solution(0))