import sys

T = int(sys.stdin.readline())

for i in range(T):
    case = sys.stdin.readline().rstrip().split()
    
    idx = len(case) - 1
    result = []

    while idx >= 0:
        result.append(case[idx])
        idx -= 1

    answer = " ".join(result)

    print(f'Case #{i+1}: {answer}')