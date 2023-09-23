# 📌 문제 013) 카드 게임
# 시간 제한 2초, 실버 IV, 백준 2164번

from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1: # 카드가 1장 남을 때까지
    myQueue.popleft() # 맨 위의 카드를 버림
    myQueue.append(myQueue.popleft()) # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(myQueue[0])