import sys
sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
max = -21470000000

#def digit_sum(x):
#    sum=0 #자릿수 더한 값
#    while x >0:
#        sum += x%10
#        x = x //10
#    return sum

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
        
for x in a:
    total = digit_sum(x)
    if total> max:
        max = total
        res = x #결과는 res

print(res)
 
