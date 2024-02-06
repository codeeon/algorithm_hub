import sys, collections

T = int(sys.stdin.readline().rstrip())

keys = ['<', '>', '-']

for i in range(T):
    case = sys.stdin.readline().rstrip()

    q1 = collections.deque()
    q2 = collections.deque()

    for char in case:
        if len(q1) > 0:
            if char == '<':
                q2.appendleft(q1.pop())
            elif char == '-':
                q1.pop()
        
        if len(q2) > 0 and char == '>':
            q1.append(q2.popleft())
        
        if char not in keys:
            q1.append(char)
    
    print(''.join(q1 + q2))