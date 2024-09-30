a, b = 1, 1

n, A, B = map(int, input().split())
# A 칭찬, B 비난

for _ in range(n):
    a += A; b += B
    if a < b:
        a, b = b, a
    if a == b:
        b -= 1

print(a, b)