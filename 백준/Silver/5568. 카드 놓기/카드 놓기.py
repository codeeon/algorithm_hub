import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

cards = [ str(sys.stdin.readline().rstrip()) for _ in range(0, n) ]

cases = set([ ''.join(i) for i in permutations(cards, k) ])

print(len(cases))