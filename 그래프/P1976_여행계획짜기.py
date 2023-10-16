# 📌 문제 051) 여행 계획 짜기
# 시간 제한 2초, 골드 IV, 백준 1976번

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [0] * (N + 1)

def find(a): # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀 형태로 구현 -> 경로 압축 부분
        return parent[a]

def union(a, b): # union 연산 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b): # 두 원소가 같은 집합에 속해 있는지 확인하는 함수
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")