import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().rstrip().split())) for _ in range(n)]
w_split_count, b_split_count = 0, 0
def paper_count(x,y,k):
    global w_split_count, b_split_count
    """
        x,y ~ x+k, y+k 까지 전부 1로 차있는지 확인
        만약 1로 차있지 않다면 다시 분할
        1로 차있다면 count += 1
    Args:
        x (int): width position
        y (int): height position
        k (int): cut position
    """
    one_count = 0
    for i in range(y,y+k): # height 먼저 접근
        for j in range(x,x+k): # width 접근 
            if arr[i][j] == 1:
                one_count += 1

    if one_count == k**2:
        b_split_count += 1
    elif one_count == 0:
        w_split_count += 1
    else:
        # 4등분 해서 계산함
        paper_count(x,y,k//2)
        paper_count(x+k//2, y,k//2)
        paper_count(x,y+k//2,k//2)
        paper_count(x+k//2,y+k//2,k//2)

paper_count(0,0,n)
print(w_split_count, b_split_count)