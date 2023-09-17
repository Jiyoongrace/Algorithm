#📌 문제 002) 평균 구하기
# 시간 제한 2초, 브론즈 I, 백준 1546번

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))