N = int(input())
T = 1
k = 0
n = 0

while (T < N):
    T = T + (6*k)
    k += 1
    n += 1

if(N == 1):
    n = 1
    # 1일 때는 while문을 들어가지 않지만
    # 등호를 넣으면 마지막 숫자의 횟수가 제대로 카운트 되지 않아
    # 1을 예외처리 해주어야함

print(n)