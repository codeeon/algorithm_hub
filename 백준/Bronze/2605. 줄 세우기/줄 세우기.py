import sys

T = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# 1. List로 풀어보기.
lst = [i for i in range(1, T+1)]

for i in range(0, T):
    cnt = 0
    j = i

    while True:
        if cnt == data[i]:
            break
        
        else:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
            cnt += 1

answer = " ".join(map(str, lst))

print(answer)