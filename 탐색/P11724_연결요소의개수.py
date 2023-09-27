# 📌 문제 023) 연결 요소의 개수 구하기
# 시간 제한 3초, 실버 V, 백준 11724번

import sys
sys.setrecursionlimit(10000) # 재귀 호출의 최대 깊이 제한을 설정하는 함수
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]: # ex) 1에 연결된 2와 5 모두 DFS 수행
        if not visited[i]:
            DFS(i)

for _ in range(m): # 그래프를 인접 리스트로 저장하기
    s, e = map(int, input().split())
    A[s].append(e) # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)