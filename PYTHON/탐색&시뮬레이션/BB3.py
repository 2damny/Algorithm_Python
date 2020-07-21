# 카드 역배치 (중요중요)

import sys
sys.stdin = open("input.txt", "rt")

# 0부터 20까지 리스트를 생성한다.
a = list(range(21))

# 입력변수를 돌면서 swap해주는 부분
# _는 변수를 사용하지 않는것
# 주어진 구간이 10개이니까 range(10)
for _ in range(10):
    s,e=map(int, input().split())
    # 입력받은 s,e가 자리를 바꾸기 위해서는 (e-s+1)//2 만큼 회전해야함
    for i in range((e-s+1)//2):
        #자리 바꿔주기(swap)
        s[s+i],s[e-i] = s[e-i],s[s+i]
# 리스트가 1부터 시작되어야 하니까 0번 인덱스 제거(.pop(0))
s.pop(0)

# 역배치되고, 0인덱스 제거된 최종 값 출력
print(a)