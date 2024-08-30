from collections import deque
import sys
def play_game():
    turn = 1
    while turn <= 1000:
        # move pieces with priority
        for pieces_num in range(k):
            check_position = move(pieces_num)
            if check_position:
                return turn
        turn += 1
    return turn

def move(pieces_num):
    d = [(0,1), (0,-1), (-1,0), (1,0)]
    pr, pc, dir = pieces[pieces_num] 
    
    dr, dc = d[dir][0], d[dir][1]
    nr, nc = pr + dr, pc + dc
    
    # blue one or out of boundery 사전 처리
    if not (0<=nr<n and 0<=nc<n) or arr[nr][nc] == 2:
        dir = dir + 1 if dir % 2 == 0 else dir -1
        dr, dc = d[dir][0], d[dir][1]
        nr, nc = pr + dr, pc + dc

    if not (0<=nr<n and 0<=nc<n):
        nr, nc = pr,pc
    # 흰색일 경우 (case white)
    elif arr[nr][nc] == 0:
        for elem in pieces_map[pr][pc]:
            pieces_map[nr][nc].append(elem)
        pieces_map[pr][pc] = deque()

    # 붉은색일 경우 (case red)
    elif arr[nr][nc] == 1:
        pieces_map[pr][pc].reverse()
        for elem in pieces_map[pr][pc]:
            pieces_map[nr][nc].append(elem)
        pieces_map[pr][pc] = deque()
    else:
        nr, nc = pr, pc

    for next_pieces_num in pieces_map[nr][nc]:
        if next_pieces_num == pieces_num:
            cur_dir = dir
        else:
            _, _, cur_dir = pieces[next_pieces_num]
        pieces[next_pieces_num] = [nr, nc, cur_dir]
    
    if len(pieces_map[nr][nc]) >=4:
        return 1
    return 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] # map_info
    pieces_map = [[deque() for _ in range(n)] for _ in range(n)] # saving pieces' num
    pieces = [[] for _ in range(k)] # saving position and dir (index means priority) 
    for i in range(k):
        px,py,dir = map(int, input().split())
        pieces[i] = [px-1, py-1, dir-1] # starting at 1
        pieces_map[px-1][py-1].append(i)
    turn = play_game()
    print(turn if turn != 1001 else -1)
