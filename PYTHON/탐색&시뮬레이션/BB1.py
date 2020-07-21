# 회문문자열 검사
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

# 1
#for i in range(n):
#    s = input() #문자열 입력받기
#    s = s.upper() #문자열을 다 대문자화 시키기(.upper)
#    size = len(s) #s의 길이를 구해주기

#    for j in range(size//2): #문자열을 2로 나누었을때의 몫만큼만회전하면 됨
#        if s[j] != s[-1-j]: #양쪽끝이 같지 않으면
#            print("#%d NO" %(i+1))
#            break
#    else: #양쪽 끝 문자가 같은 회문 문자열이면 
#        print("#%d YES" %(i+1))
        
# 2 슬라이스 기능 이해하기 
for i in range(n):
    s = input()
    s = s.upper()
    if s==s[::-1]: #[::-1]: 맨뒤에서 부터 거꾸로 비교
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
