from math import gcd

def solution(arrayA,arrayB):

    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    gcdA, gcdB = arrayA[0], arrayB[0]

    for i,j in zip(arrayA, arrayB):
        gcdA = gcd(gcdA,i)
        gcdB = gcd(gcdB,j)

    for i,j in zip(arrayA, arrayB):
        if gcdB != 0 and i % gcdB == 0 :
            gcdB = 0
        if gcdA != 0 and j % gcdA == 0:
            gcdA = 0

    return max(gcdA, gcdB)