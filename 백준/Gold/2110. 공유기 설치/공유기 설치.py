import sys

input = sys.stdin.readline
N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

def canInstall(distance):
    count = 1
    last = houses[0]
    for i in range(1, N):
        if houses[i] - last >= distance:
            count += 1
            last = houses[i]
    return count >= C

left, right = 1, houses[-1] - houses[0]

answer = 0

while left <= right:
    mid = (left + right) // 2
    if canInstall(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
