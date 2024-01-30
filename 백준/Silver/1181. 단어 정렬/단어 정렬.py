import sys

T = int(sys.stdin.readline())
cases = set([])

for i in range(T):
    case = sys.stdin.readline().rstrip()
    cases.add((len(case), case))

result = sorted(cases)

for case in result:
    print(case[1])