# 📌 문제 059) 타임머신으로 빨리 가기
# 시간 제한 1초, 골드 IV, 백준 11657번

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N + 1)

for i in range(M): # 에지 데이터만 저장
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만 포드 수행
distance[1] = 0

for _ in range(N - 1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클 확인
mCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)