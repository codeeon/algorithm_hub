import sys

T = int(sys.stdin.readline().rstrip())

task = []
score = 0

for i in range(T):
    case = list(map(int, sys.stdin.readline().rstrip().split()))

    if case[0] == 1:
        task.append([case[1], case[2]])

    if len(task) > 0:
        task[-1][1] = task[-1][1] - 1

        if task[-1][1] == 0:
            score += task[-1][0]
            task.pop()

print(score)