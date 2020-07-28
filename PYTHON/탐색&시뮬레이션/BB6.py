import sys
sys.stdin = open("input.txt","rt")


n = int(input())

# 한줄 읽어서리스트
# a = [list(map(int, input().split()))]

# n행을 n번 읽기, 리스트화 
a = [list(map(int, input().split())) for _ in range(n)]

# 가장큰 값 구하기 위해서는 가장 작은 값으로 초기
largest= -2147000000

# 행의 합(sum1), 열의 합(sum2)
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선의 합
# 위에서 밑으로 가는 대각선(sum1), 아래에서 위로 가는 대각선(sum2)

sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest =sum1
if sum2 > largest:
    largest = sum2

print(largest)
