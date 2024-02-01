import sys, heapq, collections

n = int(sys.stdin.readline().rstrip())

present = []

for i in range(n):
    a = collections.deque(sys.stdin.readline().rstrip().split())

    if a[0] == '0':
        if len(present) == 0:
            print(-1)
        else:
            print(heapq.heappop(present) * -1)
    else:
        a.popleft()
        for i in a:
            heapq.heappush(present, int(i) * -1)