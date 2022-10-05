import sys
input = sys.stdin.readline
def change_row(row): return ord(row) - ord('A')

# 스도쿠 체크
def check(sr, sc, v):
    for i in range(len(arr[0])):
        if arr[sr][i] == v:
            return False
        if arr[i][sc] == v:
            return False
        for k in range(3):
            for l in range(3):
                sr = (sr // 3) * 3
                sc = (sc // 3) * 3
                if arr[sr + k][sc + l] == v:
                    return False
    return True

def dp(idx):
    global iter
    find = False

    # 종료조건
    if idx == len(blank_arr):
        print(arr)
        return True

    r,c = blank_arr[idx]
    if arr[r][c]: 
        find = dp(idx + 1)
        return find

    for v1 in range(1,10):
        for v2 in range(1,10):
            if v1 == v2 or visited[v1][v2]: continue
            for k in range(2):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < max_arr and 0 <= nc < max_arr and not arr[nr][nc]:
                        if check(r,c,v1) and check(nr,nc,v2):
                            arr[r][c], arr[nr][nc] = v1, v2
                            visited[v1][v2] = 1
                            find = dp(idx+1)
                            if find: return find    
                            arr[r][c], arr[nr][nc] = 0, 0
                            visited[v1][v2] = 0
    return find

if __name__ == "__main__":
    n = 10
    max_arr = 9
    arr = [[0 for _ in range(max_arr)] for _ in range(max_arr)]
    blank_arr = []
    visited = [[0 for _ in range(max_arr+1)]for _ in range(max_arr+1)]
    dr = [0,1]
    dc = [1,0]

    # 초기 도미노 설정
    for _ in range(n):
        pv, pp, nv, np = input().rstrip("\n").split()
        pv,nv = int(pv), int(nv)
        prow, pcolumn = change_row(pp[0]), int(pp[1]) - 1
        nrow, ncolumn = change_row(np[0]), int(np[1]) - 1
        arr[prow][pcolumn],arr[nrow][ncolumn] = int(pv), int(nv)
        visited[int(pv)][int(nv)], visited[int(pv)][int(nv)] = 1, 1

    # 숫자 배치
    pl = input().rstrip("\n").split()
    for i,pos in enumerate(pl,start=1):
        r,c = change_row(pos[0]), int(pos[1]) - 1
        arr[r][c] = i

    # 빈칸 세기
    for i in range(max_arr):
        for j in range(max_arr):
            if not arr[i][j]:
                blank_arr.append((i,j))
    print(len(blank_arr),blank_arr)
    # SOLVE
    dp(0)