def main():
    n, k = map(int, input().split())

    lst = list(map(int, input().split()))

    if lst == [i for i in range(n)]:
        return 'Yes'

    set_ = set()
    for idx, i in enumerate(lst):
        if idx != i:
            set_.add(abs(idx-i))

    list_ = list(set_)
    for i in list_:
        if i % k != 0:
            return "No"
    else:
        return "Yes"

 
if __name__ == "__main__":
    print(main())