import sys
input = sys.stdin.readline
N = int(input())
result = [0] * N
inequal_list = list(input().rstrip("\n"))
S = [[0] * N for _ in range(N)] 

for i in range(N):
    for j in range(i, N):
        inequal_sign = inequal_list.pop(0)
        if inequal_sign == '+':
            S[i][j] = 1
        elif inequal_sign == '-':
            S[i][j] = -1

# 이 solution이 가능한지 판단하는 함수.
# 모든 inequal_sign을 판단해야 한다.

def promising(cnt):
    add_all = 0
    for idx in reversed(range(cnt+1)):
        add_all += result[idx]
        check_sign = S[idx][cnt]

        # 부호가 다르면 false
        if add_all == 0 and check_sign != 0: return False
        elif add_all > 0 and check_sign <= 0: return False
        elif add_all < 0 and check_sign >= 0: return False
    return True

def sol(cnt):
    if cnt == N: 
        print(' '.join(map(str,result)))
        exit(0)
    for i in range(1,11):    
        result[cnt] = S[cnt][cnt] * i
        if promising(cnt):
            sol(cnt+1)
        else:
            result[cnt] = 0


sol(0)