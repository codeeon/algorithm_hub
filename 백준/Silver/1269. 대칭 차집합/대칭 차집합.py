import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

X = set(A)
Y = set(B)

answer = len(X-Y) + len(Y-X)

print(answer)