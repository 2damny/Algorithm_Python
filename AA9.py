import sys
sys.stdin=open("input.txt","rt")

#사람수대로 for문을 돌면서 수행

n=int(input()) #사람숫자입력
res = 0

for i in range(n):
    tmp= input().split() #문자화된 숫자가 들어감
    tmp.sort() #세번째규칙이 가장 큰 숫자인 경우니까 그냥 오름차순 정렬해버리기~
    a, b, c = map(int, tmp) #tmp에 있는 문자화된 숫자가 int화 되어 a,b,c에 정렬

#상금이 제일 높은거 먼저 if문에 써주기
    if a==b and b==c: #규칙1
        money = 10000+(a*1000)
    elif a==b or a==c: #규칙2
        money = 1000+(a*100)
    elif b==c: #규칙2
        money = 1000+(b*100)
    else: #규칙3
        money = c*100
    if money>res: #가장큰값
        res = money

print(res)    
    
