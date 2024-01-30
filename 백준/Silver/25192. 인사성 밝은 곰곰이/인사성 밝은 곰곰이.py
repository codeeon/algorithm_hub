import sys

N = int(sys.stdin.readline().rstrip())

greet = set([])
result = 0

for i in range(N):
    chat = sys.stdin.readline().rstrip()

    if chat == "ENTER":
        result += len(greet)
        greet = set([])
    else:
        greet.add(chat)

result += len(greet)

print(result)