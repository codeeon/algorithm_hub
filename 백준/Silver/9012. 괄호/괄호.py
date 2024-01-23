import sys

T = int(sys.stdin.readline())

for i in range(T):
    case = sys.stdin.readline()
    stack = []
    result = True

#    print(case)
    
    for char in case:
        if char == '(':
            stack.append(char)
        elif len(stack) == 0 and char == ')':
            result = False
            break
        elif char == ')' and len(stack) > 0:
            stack.pop()
            
    if result == False or len(stack) > 0:
        print('NO')
    else:
        print('YES')