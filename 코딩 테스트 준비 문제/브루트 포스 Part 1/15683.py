from copy import deepcopy
def change_arr_with_cctv_dir(cctv_pos:tuple, cctv_dir:int, arr:list) -> list:
    for dir in cctv_dir:
        nx, ny = cctv_pos
        while True:
            # 이동
            nx += dir[0]
            ny += dir[1]

            # 범위 밖으로 벗어난 경우
            if not (0<=nx<n and 0<=ny<m): break
            
            # 만약 벽을 만났을 경우
            if arr[nx][ny] == 6: break

            if arr[nx][ny] == 0:
                arr[nx][ny] = -1
    return arr

# 사각지대의 수를 세주는 함수
# count blind spot
def count_blind_spot(arr:list)->int: 
    result = 0
    for i in arr:
        for j in i:
            if j == 0:
                result += 1
    return result

def dfs(prev_arr:list, depth:int) -> None:
    # end condition
    if depth == len(cctv_list):
        global min_value
        dfs_min_value = count_blind_spot(prev_arr)
        if min_value > dfs_min_value:
            min_value = dfs_min_value
        return

    next_arr = deepcopy(prev_arr)
    cctv_pos, cctv_type = cctv_list[depth]
    for cctv_dir in d[cctv_type]:

        # 변환
        next_arr = change_arr_with_cctv_dir(cctv_pos, cctv_dir, next_arr)
        dfs(next_arr, depth + 1)

        # 재탐색을 위해 되돌리기
        next_arr = deepcopy(prev_arr)

if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cctv_list = list()
    for i in range(n):
        for j in range(m):
            if arr[i][j] and arr[i][j] != 6:
                cctv_list.append(((i,j), arr[i][j])) # position and value
    L = (0,-1)
    R = (0,1)
    U = (-1,0)
    D = (1,0)

    d = {
        1: [[U],[D],[L],[R]], # type 통일
        2: [[L,R], [U,D]],
        3: [[U,R], [R,D], [L,D], [L,U]],
        4: [[L,U,R], [U,R,D], [L,D,R], [U,D,L]],
        5: [[L,R,U,D]]
    }
    min_value = 99999
    dfs(arr,0)
    print(min_value)