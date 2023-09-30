# 📌 문제 034) 수를 묶어서 최댓값 만들기
# 시간 제한 2초, 골드 IV, 백준 1744번

from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    data = int(input())
    pq.put(data)

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)

print(sum)