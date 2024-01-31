import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

deq = deque([])

for i in range(T):
    case = list(sys.stdin.readline().rstrip().split())
    
    if case[0] == 'push_front':
        deq.appendleft(case[1])

    if case[0] == 'push_back':
        deq.append(case[1])

    if case[0] == 'pop_front':
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)

    if case[0] == 'pop_back':
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)

    if case[0] == 'size':
        print(len(deq))

    if case[0] == 'empty':
        if len(deq) > 0:
            print(0)
        else:
            print(1)

    if case[0] == 'front':
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)

    if case[0] == 'back':
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)