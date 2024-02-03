import sys, math

i = 1

while True:
    data = sys.stdin.readline().rstrip()
    if '-' in data:
        break

    stack = []
    cnt = 0

    for char in data:
        if char == '{':
            stack.append(char)
        elif len(stack) > 0:
            stack.pop()
        else:
            cnt += 1
            
    answer = math.ceil(cnt / 2) + math.ceil(len(stack) / 2)

    print(f'{i}. {answer}')
    i += 1