import sys, heapq

n = int(sys.stdin.readline().rstrip())

present = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    if a[0] == 0:
        if len(present) == 0:
            print(-1)
        else:
            print(heapq.heappop(present) * -1)
    else:
        for i in range(1, len(a)):
            heapq.heappush(present, a[i] * -1)