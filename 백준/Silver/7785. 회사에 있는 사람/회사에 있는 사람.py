import sys

T = int(sys.stdin.readline().rstrip())

check = set([])

for i in range(T):
    data = list(sys.stdin.readline().rstrip().split())

    if data[1] == 'enter':
        check.add(data[0])
    else:
        check.remove(data[0])

for result in sorted(check, reverse=True):
    print(result)