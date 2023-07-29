# silver 4
# 20363번, 당근 키우기

x, y = map(int,input().split())
if x < y:
    x, y = y, x

print(x+y+y//10)