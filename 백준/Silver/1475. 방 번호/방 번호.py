import sys, math

numbers = {key:0 for key in range(0, 10)}

sixOrNine = 0
result = []

N = str(sys.stdin.readline().rstrip())

for num in N:
    numbers[int(num)] += 1

for i in numbers:
    if i == 6 or i == 9:
        sixOrNine += numbers[int(i)]
    else:
        result.append((numbers[int(i)], i))

answer = max(sorted(result, reverse=True)[0][0], math.ceil(sixOrNine / 2))

print(int(answer))