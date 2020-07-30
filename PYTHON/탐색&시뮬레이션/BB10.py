import sys
sys.stdin = open("input.txt","rt")

# 1. 행탐색, 열탐색 리스트를 사용하여 이중포문 1개만들기
# 2. 그룹탐색 리스트를 사용하여 사중포문 1개 만들기

# 1차원 체크리스트 세개 (행, 열, 그룹 검사)
# 체크리스으의 초기값은 0
# 체크리스트의 합이 9이면 값이 다 들어갔음을 의미

# check 함수 정의
def check(a):
    for i in range(9):
        # 행체크, 열체크 리스트 생성
        ch1=[0]*10
        ch2=[0]*10
        # a리스트를 탐색하면서 ch1,ch2에 체크해주기
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!= 9 or sum(ch2) !=9:
            return False
    #여기가 핵심이네 어렵네.
    # 3x3그룹을 만들어줘야지(i,j)
    for i in range(3):
        for j in range(3):
            # 그룹체크리스트 생성
            ch3 =[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3) != 9:
                return False
    return True

# 메인부분
# 9x9 격자 정보 받기
a = [list(map(int, input().split())) for _ in range(9)]
# check 함수
if check(a):
    print("YES")
else:
    print("NO")
