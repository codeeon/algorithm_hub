import sys

T = int(sys.stdin.readline())

sold = []
sales = {}

for _ in range(T):
    case = sys.stdin.readline().rstrip()
    sold.append(case)
    sales[case] = 0

for book in sold:
    sales[book] += 1

result = [(sales[b] * -1, b) for b in sales.keys()]

answer = sorted(result)

print(answer[0][1])