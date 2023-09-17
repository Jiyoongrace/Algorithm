# 📌 문제 001) 숫자의 합 구하기
# 시간 제한 1초, 브론즈 IV, 백준 11720번

n = input()
numbers = list(input())
sum = 0

for i in numbers:
	sum = sum + int(i) # numbers에 있는 각 자리 수를 가져와 더하기
    
print(sum)