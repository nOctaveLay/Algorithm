from collections import deque
import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
    
def rotate_left(arr):
    for k in range(min(n,m)//2):
        dq = deque()
        for i in range(k,m-1-k):
            dq.append(arr[k][i])
        for i in range(k,n-1-k):
            dq.append(arr[i][m-1-k])
        for i in range(m-1-k,k,-1):
            dq.append(arr[n-1-k][i])
        for i in range(n-1-k,k,-1):
            dq.append(arr[i][k])
        
        #회전
        dq.rotate(-r)

        #채우기
        
        for i in range(k,m-1-k):
            arr[k][i] = dq.popleft()
        for i in range(k,n-1-k):
            arr[i][m-1-k] = dq.popleft()
        for i in range(m-1-k,k,-1):
            arr[n-1-k][i] = dq.popleft()
        for i in range(n-1-k,k,-1):
            arr[i][k] = dq.popleft()
    return arr
rotate_left(arr)
for i in range(n):
    print(*arr[i])
        