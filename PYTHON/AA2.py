#import sys
#sys.stdin=open("input.txt","rt")

T=int(input()) #케이스 갯수
for t in range(T):
    N, s, e, k = map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e] #리스트 자르기
    a.sort() #오름차순정렬
    print("#%d %d" %(t+1, a[k-1]))
