# 📌 문제 053) 줄 세우기
# 시간 제한 2초, 골드 III, 백준 2252번

from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 배열

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1  # 집입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:  # 위상정렬 수행
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)