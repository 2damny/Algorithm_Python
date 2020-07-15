#k번째 약수 구하기

import sys
sys.stdin=open("input.txt", "rt")

#숫자가 공백(줄바꿈이 아니라)으로 들어오면 map을 써야한다. 
n,k = map(int,input().split( ))


#갯수를 세야함! cnt
cnt = 0
 
for i in range(1, n+1):
    if n%i == 0:
        cnt = cnt+1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
