# 📌 문제 021) 버블 정렬 프로그램 2
# 시간 제한 1초, 플래티넘, 백준 1517번

import sys
input = sys.stdin.readline
result = 0

def merge_sort(s, e): # 병합 정렬 수행
    global result
    if e - s < 1: return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)  # 재귀 함수의 형태로 구현
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e: # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # 뒤쪽 데이터 값이 더 작다면 결괏값 업데이트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    
    while index1 <= m: # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1
        
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * int(N+1)
merge_sort(1, N)
print(result)