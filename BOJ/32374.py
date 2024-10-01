def main():
    n, k = map(int ,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b.sort(); c.sort()

    i, j = k-1, n-1

    while i >= 0 and b[j] == c[i]:
        i -=1; j -= 1

    mx = 0; box = b[j]

    for value in a:
        if box >= value:
            if value > mx:
                mx = value

    return mx

if __name__ == "__main__":
    print(main())