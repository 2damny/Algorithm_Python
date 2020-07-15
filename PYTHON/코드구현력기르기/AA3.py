# K번째 큰 수
import sys
sys.stdin=open("input.txt","rt")


N, K = map(int,input().split())
a = list(map(int,input().split()))
#a = list(set(a))  #list(set(a)) set은 중복제거

res = set()


'''
세개의 자료를 뽑아서 res에 넣기(삼중포문)
'''
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            res.add(a[i]+a[j]+a[k])
            #set자료구조는 uppend가 아니라 add 사용

res = list(res) #set자료구조는 sort기능이 없으니까 list로 다시 만들어주기
res.sort(reverse=True)
print(res[K-1])
