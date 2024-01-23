import sys, math

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    a, b = abs(x1 - x2), abs(y1 - y2)
    dist = math.sqrt(pow(a, 2) + pow(b, 2))

#    print(dist)

    if dist == 0 and r1 == r2:
        print(-1)
    elif r1 == dist + r2 or r2 == dist + r1:
        print(1)
    elif r1 + r2 == dist:
        print(1)
    elif r1 + r2 > dist and dist == 0:
        print(0)
    elif r1 > dist + r2 or r2 > dist + r1:
        print(0)
    elif r1 + r2 > dist:
        print(2)
    else:
        print(0)