# silver
# 과제는 끝나지 않아!
import sys

def main():
    n = int(input().rstrip())

    task, ans = [], 0

    for __ in range(n):
        new_task = list(map(int, input().rstrip().split()))
        if new_task[0] == 1:
            if new_task[2] == 1:
                ans += new_task[1]
            else:
                task.append((new_task[1], new_task[2]-1))
        elif new_task[0] == 0 and len(task) > 0:
            score, time = task.pop()
            time -= 1
            if time == 0:
                ans += score
            elif time != 0:
                task.append((score, time))

    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    print(main())