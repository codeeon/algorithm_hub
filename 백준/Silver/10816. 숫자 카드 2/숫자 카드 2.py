import sys
import bisect

input = sys.stdin.read
data = list(map(int, input().split()))

N = data[0]
A = sorted(data[1:N+1])
M = data[N+1]
X = data[N+2:]

result = []

for x in X:
    left = bisect.bisect_left(A, x)
    right = bisect.bisect_right(A, x)
    count = right - left
    result.append(str(count))

print(' '.join(result))
