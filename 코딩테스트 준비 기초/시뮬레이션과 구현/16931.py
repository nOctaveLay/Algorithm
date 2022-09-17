import sys
input = sys.stdin.readline

def return_surface_area(ns):

# 한 방향만 편하게 계산해주기 위하여, 양수만 계산해주기로 한다.
# 가로 방향으로 움직였을 경우
    column_sum = 0
    for i in range(n):
        for j in range(m):
            if j < m-1:
                diff = ns[i][j] - ns[i][j+1]
            else: diff = ns[i][j]
            if not diff < 0 :
                column_sum += diff

    row_sum = 0
    for j in range(m):
        for i in range(n):
            if i < n-1:
                diff = ns[i][j] - ns[i+1][j]
            else:
                diff = ns[i][j]
            if not diff < 0:
                row_sum += diff

    return row_sum*2+column_sum*2+n*m*2
if __name__ == "__main__":
    n, m = map(int,input().split())
    ns = [list(map(int,input().split())) for _ in range(n)]
    print(return_surface_area(ns))