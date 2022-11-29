from copy import deepcopy
from itertools import permutations

def rotate_matrix(arr:list,r:int,c:int,s:int) -> list:
    lev = 1
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    while lev < s + 1:
        sr, sc = r - lev, c - lev
        sr -= 1
        sc -= 1
        prev_value = arr[sr][sc]
        for dr, dc in d:
            for _ in range(lev * 2):
                nr, nc = sr + dr, sc + dc
                next_value = arr[nr][nc]
                arr[nr][nc] = prev_value
                prev_value = next_value
                sr, sc = nr, nc
        lev += 1
    return arr

def get_arr_min_value(arr:list) -> int:
    min_value = 101 * m
    for i in arr:
        min_value = min(min_value, sum(i))            
    return min_value


if __name__ == "__main__":
    n, m, k = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(n))
    rotate_operations = list(tuple(map(int,input().split())) for _ in range(k))
    min_value = 101 * m
    for permutate in permutations(rotate_operations):
        temp_arr = deepcopy(arr)
        for elem in permutate:
            temp_arr = rotate_matrix(temp_arr,*elem)
        min_value = min(get_arr_min_value(temp_arr), min_value)
    print(min_value)