# 📌 문제 008) '좋은 수' 구하기
# 시간 제한 2초, 골드 IV, 백준 1253번

import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j: # 투 포인터 알고리즘
        if A[i] + A[j] == find: # find는 서로 다른 두 수의 합이어야 함을 체크
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)