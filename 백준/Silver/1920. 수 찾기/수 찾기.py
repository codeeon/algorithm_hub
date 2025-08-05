import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = sorted(map(int, data[1:N+1]))
M = int(data[N+1])
X = list(map(int, data[N+2:]))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for x in X:
    print(binary_search(A, x))
