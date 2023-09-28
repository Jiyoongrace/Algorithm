# 📌 문제 028) 트리의 지름 구하기
# 시간 제한 2초, 골드 III, 백준 1167번

from collections import deque
N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index + 1]
        A[S].append((E, V))
        index += 2 # -1 이 되면서 while 루프 종료

distance = [0] * (N+1)
visited = [False] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1] # 거리 리스트 업데이트

BFS(1)
Max = 1

for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N+1)
visited = [False] * (N+1)
BFS(Max)
distance.sort()
print(distance[N])