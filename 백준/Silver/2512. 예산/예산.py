import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

def isPossible(cap):
    return sum(min(b, cap) for b in budgets) <= M

left = 0
right = max(budgets)
answer = 0

while left <= right:
    mid = (left + right) // 2
    if isPossible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
