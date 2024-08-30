# PYPY에서는 정상적으로 돌아가나, python에서는 안 돌아감

import sys
input = sys.stdin.readline

# 같은 열에서 행을 체크
def check_row(v,sc):
    for i in range(len(arr[0])):
        if arr[i][sc] == v:
            return False
    return True

# 같은 행에서 열을 체크
def check_column(v,sr):
    for i in range(len(arr)):
        if arr[sr][i] == v:
            return False
    return True 

# 정사각형에서 행/열을 체크
def check_rectangle(r,c,v):
    r //= 3
    c //= 3
    for i in range(3):
        for j in range(3):
            if arr[r*3+i][c*3+j] == v:
                return False
    return True

def check_blank():
    result = list()
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                result.append((i,j))
    return result

def dfs(idx):
    
    if idx == len(blank):
        for i in arr:
            print(*i)
        exit(0)

    r, c = blank[idx][0], blank[idx][1]
    for i in range(1,10):
        if check_row(i,c) and check_column(i,r) and check_rectangle(r,c,i):
            arr[r][c] = i
            dfs(idx+1)
            arr[r][c] = 0

if __name__ == "__main__":
    arr = [list(map(int,input().split())) for _ in range(9)]
    blank = check_blank()
    dfs(0)


