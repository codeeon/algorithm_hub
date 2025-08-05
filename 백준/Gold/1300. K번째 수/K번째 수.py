import sys

input = sys.stdin.readline
N = int(input())
k = int(input())

def countLessOrEqual(x):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, x // i)
    return cnt

left, right = 1, N * N
answer = 0

while left <= right:
    mid = (left + right) // 2
    if countLessOrEqual(mid) >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
