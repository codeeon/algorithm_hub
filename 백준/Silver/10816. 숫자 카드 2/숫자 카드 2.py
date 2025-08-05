import sys

input = sys.stdin.read
data = list(map(int, input().split()))

N = data[0]
A = sorted(data[1:N+1])
M = data[N+1]
X = data[N+2:]

def lowEnd(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def highEnd(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

result = []

for x in X:
    count = highEnd(A, x) - lowEnd(A, x)
    result.append(str(count))

print(' '.join(result))
