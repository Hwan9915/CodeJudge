def main():
    vec = set()
    lst = [input() for _ in range(36)]
    for i in lst:
        if i in vec:
            return 'Invalid'
        vec.add(i)
    lst.append(lst[0])
    map_dict = {'A' : 1, 'B' : 2, 'C' : 3, 'D': 4, 'E': 5, 'F': 6,
                '1' : 1, '2' : 2, '3' : 3, '4': 4, '5': 5, '6': 6}

    

    for i in range(1,37):
        before = map_dict[lst[i-1][0]], map_dict[lst[i-1][1]]
        
        now = map_dict[lst[i][0]], map_dict[lst[i][1]]
        

        if (abs(before[0] - now[0]) == 2 and abs(before[1] - now[1]) == 1) or (abs(before[0] - now[0]) == 1 and abs(before[1] - now[1]) == 2):
            continue
        else:
            return 'Invalid'
    return "Valid"    

if __name__ == "__main__":
    print(main())