import sys

T = int(sys.stdin.readline().rstrip())

lst = [ int(sys.stdin.readline().rstrip()) for _ in range(0, T) ]

stack = []

for _ in range(0, T):
    if len(stack) == 0:
        stack.append(lst.pop())
    elif lst[-1] > stack[-1]:
        stack.append(lst.pop())
    else:
        lst.pop()
    
print(len(stack))
