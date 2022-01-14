import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker_list = [list(map(int,input().split())) for _ in range(2)]

    # solve[n][i]:
    # i == 0 : 선택 x
    # i == 1 : 위 선택
    # i == 2 : 아래 선택
    solve = [[0,0,0] for _ in range(n)]

    # 초기 조건
    solve[0][0] = 0
    solve[0][1] = sticker_list[0][0]
    solve[0][2] = sticker_list[1][0]

    for i in range(1,n):
        solve[i][0] = max(solve[i-1][0], solve[i-1][1], solve[i-1][2])
        solve[i][1] = max(solve[i-1][0],solve[i-1][2]) + sticker_list[0][i]
        solve[i][2] = max(solve[i-1][0], solve[i-1][1]) + sticker_list[1][i]

    print(max(solve[n-1]))