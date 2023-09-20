# 📌 문제 007) 주몽의 명령
# 시간 제한 2초, 실버 IV, 백준 1940번

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
j = N-1

while i < j: # 투 포인터 이동 원칙에 따라 포인터 이동하며 처리
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)