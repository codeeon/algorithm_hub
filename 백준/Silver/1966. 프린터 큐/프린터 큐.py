from collections import deque

case = int(input())  # 최초 정수 1개, 테스트 케이스의 수

for _ in range(case):
    n, m = map(int, input().split())  # 정수 1개, 문서의 개수, 정수 1개, 현재 Queue에서 m번째 문서
    imp = list(map(int, input().split()))  # 리스트 1개, 문서 중요도 (길이 = n)

    q = deque()  # 데크
    for i, j in enumerate(imp):  # 튜플로 imp의 idx와 val를 변수 지정.
        # print((i, j))  # 체크
        q.append((i, j))  # q에 튜플 추가
    imp.sort()  # 우선순위(val == j) 정렬 (어차피 이 순서로 출력됨)
    cnt = 0
    while q:  # 후순위로 돌아간 값까지 돌 수 있게.
        a, b = q.popleft()  # q는 맨 처음 imp와 동일한 순서를 가짐. a가 idx, b가 val - idx순
        if b == imp[-1]:  # b(val)가 imp[-1] = 최우선순위면, 
            imp.pop()  # 최우선순위 제거 -> 반복
            cnt += 1  # 1순위 -> 다음 순위는 2순위
            if a == m:  # 정답(출력기대값)의 idx인 m과 제거한 값의 a(idx)가 같으면   
                print(cnt)  # cnt 출력 (cnt == 실제 출력 순서)
                break
        else:  # b가 최우선순위가 아닐 때,
            q.append((a, b))  # q의 뒤쪽으로 추가 (후순위로)