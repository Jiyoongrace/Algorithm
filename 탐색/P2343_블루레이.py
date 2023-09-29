# 📌 문제 030) 블루레이 만들기
# 시간 제한 2초, 실버 I, 백준 2343번

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i # 레슨 최댓값을 시작 인덱스로 저장
    end += i # 모든 레슨의 총합을 종료 인덱스

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(N): # 중간값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)