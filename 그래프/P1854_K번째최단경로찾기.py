# 📌 문제 058) K번째 최단 경로 찾기
# 시간 제한 2초, 플래티넘, 백준 1854번

import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
W = [[] for _ in range(N + 1)]
# 거리 리스트를 충분히 큰 값으로 초기화
distance = [[sys.maxsize] * K for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    W[a].append((b, c))

pq = [(0, 1)] # 가중치 우선이기 때문에 가중치, 목표 노드 순서로 저장
distance[1][0] = 0

while pq: # 변형된 다익스트라 수행
    cost, node = heapq.heappop(pq)
    for nNode, nCost in W[node]:
        sCost = cost + nCost
        if distance[nNode][K-1] > sCost:
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1, N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])