# 📌 문제 012) 오큰수 구하기
# 시간 제한 1초, 골드 IV, 백준 17298번
import sys

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]   # 정답 배열에 오큰수를 현재 수열로 저장하기
    myStack.append(i)

while myStack:  # 반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 빌 때까지
    ans[myStack.pop()] = -1 # 스택에 쌓인 index에 -1을 넣기

for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")