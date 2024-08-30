import sys
input = sys.stdin.readline

def flip(px,py,arr):
    for i in range(3):
        for j in range(3):
            arr[px+i][py+j] = 0 if arr[px+i][py+j] == 1 else 1
    return arr

def solution(n,m,arr_a,arr_b):
    cnt = 0
    if n < 3 or m < 3:
        if arr_a == arr_b: return 0
        else: return -1

    for i in range(n):
        for j in range(m):
            if arr_a[i][j] != arr_b[i][j]:
                if i+2 < n and j+2 < m:
                    flip(i,j,arr_a)
                    cnt += 1
                else: return -1
    return cnt
    
    


if __name__ == "__main__":
    n, m = map(int,input().split())
    arr_a = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    arr_b = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    print(solution(n,m,arr_a,arr_b))