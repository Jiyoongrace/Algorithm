# 📌 문제 022) 수 정렬하기 3
# 시간 제한 3초, 실버 V, 백준 10989번

import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]): # 해당 index값 만큼 index를 반복하여 출력
            print(i)