# 📌 문제 015) 수 정렬하기 1
# 시간 제한 2초, 브론즈 I, 백준 2750번

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])