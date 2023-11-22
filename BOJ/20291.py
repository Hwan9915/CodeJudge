# silver
# 파일 정리
import sys

def main():
    n = int(input())
    file = dict()
    for _ in range(n):
        file_name, file_extension = input().rstrip().split('.')
        if file_extension not in file:
            file[file_extension] = 1
        else:
            file[file_extension] += 1
    file_extension_lst = sorted(file.keys())
    for i in file_extension_lst:
        print(f'{i} {file[i]}\n')

if __name__ == '__main__':
    input = sys.stdin.readline
    print = sys.stdout.write
    main()