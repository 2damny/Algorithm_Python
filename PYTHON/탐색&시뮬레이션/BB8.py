import sys
sys.stdin = open("input.txt", "rt")

# 곳감(모래시계)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    # 회전처리
    # 행번호 h, 방향 t, 갯수 k
    h,t,k = map(int, input().split())
    if t == 0:
        # t가 0이면 왼쪽방향으로
        for _ in range(k):
            # 한번 회전
            # pop() : 맨 마지막요소를 출력하고, 리스트에서 삭제
            # pop(0) : 맨 앞 요소를 출력하고, 리스트에서 삭제
            # append(x) : 리스트에 요소추가
            a[h-1].append(a[h-1].pop(0))            
    # t가 1이면 오른쪽 방향으로
    # insert(a,b) : a위치에 b 삽입
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

# 모래시계합
s=0
e=n-1
res = 0
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i< n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
