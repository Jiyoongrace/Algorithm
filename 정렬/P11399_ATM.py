# 📌 문제 018) ATM 인출 시간 계산하기
# 시간 제한 1초, 실버 III, 백준 11399번

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N): # 삽입 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1): # i-1~0 까지 역순으로 반복
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1): # i~insert_point+1 까지 역순으로 반복
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N): # 합 배열 만들기
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N): # 합 배열 총합 구하기
    sum += S[i]

print(sum)