import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def isPossible(height):
    return sum((tree - height) for tree in trees if tree > height) >= M

left, right = 0, max(trees)

answer = 0

while left <= right:
    mid = (left + right) // 2
    if isPossible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
