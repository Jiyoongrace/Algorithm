# 📌 문제 054) 게임 개발하기
# 시간 제한 2초, 골드 III, 백준 1516번

from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 리스트
selfBuild = [0] * (N + 1)  # 자기자신을 짓는데 걸리는 시간

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  # 건물을 짓는데 걸리는 시간
    index = 1
    while True:  # 인접리스트 만들기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1  # 진입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  # 위상정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + selfBuild[i])