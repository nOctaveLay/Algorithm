import sys
input = sys.stdin.readline

n,m = map(int,input().split())


init_list = [list(map(int,input().rstrip("\n").split())) for _ in range(n)]

axis_list = [tuple(map(int,input().rstrip("\n").split())) for _ in range(m)]

sum_list = [[0] * n for _ in range(n)]

sum_list[0][0] = init_list[0][0]
# sum_list 초기화
for i in range(n):
    if i > 0:
        sum_list[i][0] = sum_list[i-1][0] + init_list[i][0]
    for j in range(1,n):
        if i == 0:
            sum_list[i][j] = sum_list[i][j-1] + init_list[i][j]
        else:
            sum_list[i][j] = sum_list[i-1][j] + sum_list[i][j-1] - sum_list[i-1][j-1] + init_list[i][j]

for (x1,y1,x2,y2) in axis_list:

    result = sum_list[x2-1][y2-1]
    if x1 == 1 and y1 == 1:
        print(result)
    elif x1 == 1:
        print(result - sum_list[x2-1][y1-2])
    elif y1 == 1:
        print(result - sum_list[x1-2][y2-1])
    else:
        print(result - sum_list[x1-2][y2-1] - sum_list[x2-1][y1-2] + sum_list[x1-2][y1-2])