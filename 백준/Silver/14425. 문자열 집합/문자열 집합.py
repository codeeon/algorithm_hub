import sys

N, M = map(int, (sys.stdin.readline().rstrip().split()))

S = set()
cnt = 0

for _ in range(N):
    strs = sys.stdin.readline().rstrip()
    S.add(strs)

for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        cnt += 1

print(cnt)