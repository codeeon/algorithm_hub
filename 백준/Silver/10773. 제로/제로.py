import sys

T = int(sys.stdin.readline())

stack = []
result = 0

for _ in range(T):
    case = int(sys.stdin.readline().rstrip())

    if case == 0:
        stack.pop()
    else:
        stack.append(case)

for i in stack:
    result += i

print(result)