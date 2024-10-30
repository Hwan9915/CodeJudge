def calc_tshirt_bundles(sizes, T):
    bundles = 0
    for size in sizes:
        # 각 사이즈별로 필요한 묶음 수 계산 (올림)
        bundles_needed = (size + T - 1) // T
        bundles += bundles_needed
    return bundles

def calc_pen_bundles(N, P):
    # 최대 묶음 수 계산
    max_bundles = N // P
    # 나머지 계산
    remaining = N % P
    return max_bundles, remaining

# 입력 처리
N = int(input())
sizes = list(map(int, input().rstrip().split()))  # S, M, L, XL, XXL, XXXL
T, P = map(int, input().rstrip().split())

# 티셔츠 묶음 수 계산
tshirt_bundles = calc_tshirt_bundles(sizes, T)

# 펜 묶음 수와 남은 개수 계산
pen_bundles, pen_singles = calc_pen_bundles(N, P)

print(tshirt_bundles)
print(pen_bundles, pen_singles)