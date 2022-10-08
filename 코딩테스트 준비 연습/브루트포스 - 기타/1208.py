
from collections import defaultdict

def partial_sum(idx,end,side,idx_sum):
    global s, cnt
    if idx == end: 
        if side == 'L':
            l[idx_sum] += 1
        elif s - idx_sum in l: # side == 'R'
            cnt += l[s-idx_sum]
        return
    partial_sum(idx+1,end,side,idx_sum+arr[idx])
    partial_sum(idx+1,end,side,idx_sum)


if __name__ == "__main__":
    n, s = map(int,input().split())
    l = defaultdict(int)
    cnt = 0
    arr = list(map(int,input().split()))
    partial_sum(0,n//2,'L',0)
    partial_sum(n//2,n,'R',0)
    if s == 0:
        cnt -= 1
    print(cnt)