# 📌 문제 037) 소수 구하기
# 시간 제한 2초, 실버 III, 백준 1929번

import math
M, N = map(int, input().split())
A = [0] * (N+1)

for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(N)) + 1): # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i+i, N+1, i): # 배수 지우기
        # i+i는 i의 배수, i+i부터 N까지의 범위에서 i간격으로 i의 배수를 선택
        A[j] = 0

for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])