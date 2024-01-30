import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

site = {}

for _ in range(N):
    data = sys.stdin.readline().rstrip().split()
    site[data[0]] = data[1]

for _ in range(M):
    findPw = sys.stdin.readline().rstrip()
    print(site[findPw])