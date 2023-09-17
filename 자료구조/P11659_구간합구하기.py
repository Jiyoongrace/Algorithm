# 📌 문제 003) 구간 합 구하기 1
#v 시간 제한 0.5초, 실버 III, 백준 11659번

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])