
def main():
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    # a 잡기
    if 0 != a[0] and 0 != a[1]:
        return 2
    elif a[0] < b[0] or a[1] < b[1]:
        return 1
    else:
        return 3

if __name__ == "__main__":
    print(main())