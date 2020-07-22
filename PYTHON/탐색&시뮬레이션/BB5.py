# 수들의 합
# 알고리즘 이해가 안된다. 꼭 다시 봐보기
# 강의 뭔소리지

import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt=0
rt=1

cnt= 0
tot = a[0]

while True:
    if tot < m:
        if rt<n:
            tot += a[rt]
            rt +=1
        else: #rt가 n이 될때
             break
    elif tot == m :
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)
