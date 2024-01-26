import sys, collections

T = int(sys.stdin.readline())
lst = collections.deque([i for i in range(1, T + 1)])
result = []
answer = []
flag = True

for i in range(T):
    case = int(sys.stdin.readline())

    while True:
        if len(result) == 0:
            result.append(lst.popleft())
            answer.append('+')
        if result[-1] == case:
            break

        if len(lst) == 0 and result[-1] != case:
            flag = False
            break

        result.append(lst.popleft())
        # print(result, result[-1])
        answer.append('+')

    result.pop()
    answer.append('-')

if flag:
    for i in answer:
        print(i)
else:
    print('NO')