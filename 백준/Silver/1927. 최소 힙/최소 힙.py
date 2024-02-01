import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())

heap = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x)