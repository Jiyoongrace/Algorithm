# 📌 문제 044) 칵테일 만들기
# 시간 제한 2초, 골드 II, 백준 1033번

N = int(input())
A = [[] for _ in range(N)]
visited = [False] * (N)
D = [0] * (N)
lcm = 1

def gcd(a, b): # 최대 공약수 함수 구현
    if b ==0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v): # DFS 탐색 함수 구현
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1] # // : 몫 연산자
            DFS(next)

for i in range(N-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것

D[0] = lcm
DFS(0)
mgcd = D[0]

for i in range(1, N):
    mgcd = gcd(mgcd, D[i])

for i in range(N):
    print(int(D[i] // mgcd), end=' ')