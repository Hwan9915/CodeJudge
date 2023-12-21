# silver
# 폴리오미노
import sys


def cal(tmp):
    len_tmp = len(tmp)
    if len_tmp % 2 == 1:
        print(-1)
        exit()
    tmp = ''.join(tmp)
    a, b = len_tmp // 4, (len_tmp - (len_tmp // 4) * 4) // 2
    ans = "AAAA" * a + "BB" * b
    return ans


def main():
    input_str = list(input().rstrip())

    ans = []

    tmp = []
    for i in input_str:
        if i == 'X':
            tmp.append(i)
        elif i == '.':
            result = cal(tmp)
            if result == -1:
                print(-1)
                exit()
            ans.append(result)
            ans.append('.')
            tmp = []
    if tmp != []:
        ans.append(cal(tmp))

    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    ans = main()
    print(''.join(ans))
