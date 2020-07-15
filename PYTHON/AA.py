import sys
sys.stdin = open("input.txt","rt")

s= input()
res = 0

for x in s:
    if x.isdecimal():#isdigit 숫자형태는 다 찾아주는 함수, isdecimal은 0부터 9까지만
        res=res*10+int(x)
print(res)

cnt=0
for i in range(1,res+1):
    if res%i == 0:
        cnt += 1
print(cnt)
