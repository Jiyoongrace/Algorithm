# 📌 문제 032) 동전 개수의 최솟값 구하기
# 시간 제한 1초, 실버 III, 백준 11047번

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N - 1, -1, -1): # 역순으로 출력
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)