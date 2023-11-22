# bronze
# 애너그램
import sys

def main():

    n = int(input())
    for _ in range(n):
        a, b = map(list,input().rstrip().split())
        a_sorted = sorted(a)
        b_sorted = sorted(b)

        if a_sorted == b_sorted:
            print(f"{''.join(a)} & {''.join(b)} are anagrams.\n")

        else:
            print(f"{''.join(a)} & {''.join(b)} are NOT anagrams.\n")

if __name__ == '__main__':
    input = sys.stdin.readline
    print = sys.stdout.write
    main()