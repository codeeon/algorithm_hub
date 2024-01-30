import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

n = set([])
m = set([])

for i in range(N):
    a = sys.stdin.readline().rstrip()
    n.add(a)

for i in range(M):
    a = sys.stdin.readline().rstrip()
    m.add(a)

print(len(n & m))
for i in sorted(n & m):
    print(i)