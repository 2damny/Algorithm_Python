'''
많이 어려웠음 꼭 이해하고 넘어가기
'''
# 대푯값

import sys
sys.stdin=open("input.txt", "rt")


n=int(input())
a = list(map(int,input().split()))

avg = round(sum(a)/n)
min=21470000000 
 
for idx, x in enumerate(a): #enumerate(a)는 a의 값에 인덱스도 매겨준다
    tmp = abs(x-avg) #각 점수와 평균사이의 거리 (적은 수일수록 평균과 가까운 점수)
    if tmp<min: 
        min = tmp
        score =x #평균과 가장 가까운 값을 score에 저장 
        res = idx+1 #가장 가까운 값을 가지고 있는 인덱스(학생번호) 출력
    elif tmp == min:
        if x >score:
            score = x;
            res = idx+1
print(avg, res)
 
