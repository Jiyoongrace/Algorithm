# 📌 문제 043) 최대 공약수 구하기
# 시간 제한 2초, 실버 II, 백준 1850번

def gcd(a, b):
    if b ==0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
result = gcd(a, b)

while result > 0: # result 값만큼 반복하여 1 출력
    print(1, end='')
    result -= 1