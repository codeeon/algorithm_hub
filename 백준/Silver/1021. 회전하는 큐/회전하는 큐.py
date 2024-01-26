import sys, collections

N, M = map(int, (sys.stdin.readline().split()))
# print(N, T)
cases = sys.stdin.readline().split(' ')
cases[-1] = cases[-1].split('\n')[0]
# print(cases)

lst = collections.deque([i for i in range(1, N+1)])

cnt = 0

for i in range(M):

    while True:
        if int(cases[i]) == lst[0]:
            lst.popleft()
            break
        if lst.index(int(cases[i])) > len(lst) / 2:
            lst.appendleft(lst.pop())
            cnt += 1
        else:
            lst.append(lst.popleft())
            cnt += 1

print(cnt)

q = collections.deque([])