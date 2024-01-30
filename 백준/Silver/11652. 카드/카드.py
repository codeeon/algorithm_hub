import sys

T = int(sys.stdin.readline().rstrip())

cardList = {}
cards = [ int(sys.stdin.readline().rstrip()) for _ in range(0, T) ]

for card in cards:
    cardList[card] = 0

for card in cards:
    cardList[card] += 1

result = []

for key in cardList:
    result.append((cardList[key] * -1, key))

print(sorted(result)[0][1])