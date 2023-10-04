# 📌 문제 042) 최소 공배수 구하기
# 시간 제한 1초, 실버 V, 백준 1934번

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # 재귀 형태로 구현

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))