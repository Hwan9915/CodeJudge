def main():
    n, m = map(int, input().split())
    lst = []

    for a in range(1, n+1):
        for b in range(1, n+1):
            lst.append((a,b))
    na_lst = [tuple(map(int, input().split())) for _ in range(m)]

    for x,y,d in na_lst:
        new_lst = []
        if d == 1:
            for a in lst:
                if a[0] < x and a[1] == y:
                    new_lst.append(a)
        if d == 2:
            for a in lst:
                if a[0] < x and a[1] > y:
                    new_lst.append(a)
        if d == 3:
            for a in lst:
                if a[0] == x and a[1] > y:
                    new_lst.append(a)
        if d == 4:
            for a in lst:
                if a[0] > x and a[1] > y:
                    new_lst.append(a)
        if d == 5:
            for a in lst:
                if a[0] > x and a[1] == y:
                    new_lst.append(a)
        if d == 6:
            for a in lst:
                if a[0] > x and a[1] < y:
                    new_lst.append(a)
        if d == 7:
            for a in lst:
                if a[0] == x and a[1] < y:
                    new_lst.append(a)
        if d == 8:
            for a in lst:
                if a[0] < x and a[1] < y:
                    new_lst.append(a)
        lst = new_lst
    print(lst[0][0], lst[0][1])


if __name__ == "__main__":
    main()