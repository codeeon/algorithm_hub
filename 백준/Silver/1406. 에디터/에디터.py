import sys, collections

strs = list(map(str, sys.stdin.readline().rstrip()))
T = int(sys.stdin.readline().rstrip())

q1 = collections.deque(strs)
q2 = collections.deque()

for i in range(T):
    case = list(map(str, sys.stdin.readline().rstrip().split()))

    if (case[0] == 'L' or case[0] == 'B') and len(q1) > 0:
        if case[0] == 'B':
            q1.pop()
        else:
            q2.appendleft(q1.pop())
    
    elif case[0] == 'D' and len(q2) > 0:
        q1.append(q2.popleft())

    elif case[0] == 'P':
        q1.append(case[1])

print(''.join(q1 + q2))