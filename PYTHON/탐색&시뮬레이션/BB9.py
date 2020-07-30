import sys
sys.stdin = open("input.txt", "rt")

# 상하좌우 탐색하기 위해 편리한 dx,dy리스트 생성
# 순서대로 12시 3시 6시 9시 방향탐색
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n= int(input())
a=[list(map(int, input().split())) for _ in range(n)]

# 1.가장자리 0으로 만들기
# 맨위에 0으로
a.insert(0,[0]*n)
# 맨아래 0으로
a.append([0]*n)
# 맨앞과 맨뒤
for x in a:
    x.insert(0,0)
    x.append(0)

cnt = 0
# 2.각 셀마다 상하좌우 탐색비교
# all은 ()안의 조건이 모두 참일 때 참
# k는 0부터 3까지
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
               cnt += 1
               
print(cnt)
