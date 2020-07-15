import sys
sys.stdin=open("input.txt","rt")

def reverse(x):
    res = 0
    while x>0:
        t =x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):#어떤 수 의 약수는 1과 자기자신을 제외하면 자기자신의 1/2 안에서 나온다
        if x%i == 0:
            return False
    else:
        return True
    
n = int(input())
a = list(map(int,input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
