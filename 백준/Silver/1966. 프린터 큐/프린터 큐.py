from collections import deque

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))

    q = deque()
    
    for i, j in enumerate(imp):
        q.append((i, j))
        
    imp.sort()
    
    cnt = 0
    
    while q:
        a, b = q.popleft()
        
        if b == imp[-1]:
            imp.pop()
            cnt += 1
            
            if a == m:
                print(cnt)
                break
        else:
            q.append((a, b))