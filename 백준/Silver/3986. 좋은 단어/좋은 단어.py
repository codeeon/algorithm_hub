import sys

N = int(sys.stdin.readline())

cnt = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    stack = []
    
    for char in word:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if len(stack) == 0:
        cnt += 1

print(cnt)