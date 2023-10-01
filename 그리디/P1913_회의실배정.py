# 📌 문제 035) 회의실 배정하기
# 시간 제한 2초, 실버 I, 백준 1931번

N = int(input())
A = [[0] * 2 for _ in range(N)]

for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E # 종료 시각 우선 정렬이 먼저이므로 0번째에 종료 시각을 먼저 저장
    A[i][1] = S

A.sort()
count = 0
end = -1 # 초기값을 -1로 설정하면 첫 번째 회의는 언제나 배정 가능하도록 한다.

for i in range(N):
    # 현재 검사하고 있는 회의의 시작 시각이 현재까지 배정된 회의의 종료 시각보다 뒤에 있다면,
    # 회의를 배정할 수 있다.
    if A[i][1] >= end: # 겹치지 않는 다음 회의가 나온 경우
        end = A[i][0] # 종료 시각 업데이트
        count += 1

print(count)