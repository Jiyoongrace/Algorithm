# 📌 문제 049) 물의 양 구하기
# 시간 제한 1초, 골드 V, 백준 2251번

from collections import deque
# 두 리스트를 이용하여 6가지 이동 케이스를 간편하게 정의할 수 있다.
# 여기에서 0, 1, 2는 각각 A, B, C 물통을 뜻한다.
# 예시: index = 0의 경우 Sender[0]: 0, Receiver[0]: 1이기 때문에 A -> B 케이스를 뜻한다.

Sender = [0, 0, 1, 1, 2, 2]
Receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)] # 물통 부피 용량 최대 200리터
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while queue:
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B # C는 전체 물의 양에서 A와 B를 뺀 것
        for k in range(6): # A -> B, A -> C, B -> A, B -> C, C -> A, C -> B
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]]
            next[Sender[k]] = 0
            if next[Receiver[k]] > now[Receiver[k]]: # 물이 넘칠 때
                # 초과하는 만큼 다시 이전 물통에 넣 주기
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]] = now[Receiver[k]] # 대상 물통 최대로 채우기
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0: # A의 물의 양이 0일 때 C의 물의 무게를 정답 변수에 저장
                    answer[next[2]] = True

BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')