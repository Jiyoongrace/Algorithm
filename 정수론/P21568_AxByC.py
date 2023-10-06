# 📌 문제 045) Ax+By=C
# 시간 제한 1초, 골드 I, 백준 21568번

a, b, c = map(int, input().split())
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def Execute(a, b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = Execute(b, a % b) # 재귀 형태로 유클리드 호제법 수행
    ret[0] = v[1] # 역순으로 올라오면서 x, y를 계산하는 로직
    ret[1] = v[0] - v[1] * q
    return ret

mgcd = gcd(a, b)

if c % mgcd != 0:
    print(-1)
else:
    mok = int(c / mgcd)
    ret = Execute(a, b)
    print(ret[0] * mok, end=' ')
    print(ret[1] * mok)