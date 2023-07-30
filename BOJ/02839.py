# silver
# 2839번, 설탕 배달
kg=int(input())
kg_n=kg%5
kg_m=kg//5
if kg_n==0:
    print(kg_m)
elif kg_n==1:
    kg=kg-5
    if kg<0:
        print('-1')
    else:
        print(kg_m+1)
elif kg_n==2:
    kg=kg-10
    if kg<0:
        print('-1')
    else:
        print(kg_m+2)
elif kg_n==3:
    print(kg_m+1)
else:
    kg=kg-5
    if kg<0:
        print('-1')
    else:
        print(kg_m+2)