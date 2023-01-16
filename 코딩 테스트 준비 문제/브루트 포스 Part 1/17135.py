from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

# 적을 공격, 공격 받은 적을 셈 -> return cnt
def attack_enemy(field: list, archer_positions: list, D:int):
    dead_enemy_position = set()
    
    # 궁수별 가까운 적 공격
    for archer_position in archer_positions:
        archer_r, archer_c = archer_position
        for d in range(1,D+1):
            check = 0
            for i in range(-(d-1), d):
                nr, nc = archer_r-(d-abs(i)), archer_c + i
                if not (0<=nr<n and 0<=nc<m): continue
                if field[nr][nc] == 1:
                    dead_enemy_position.add((nr, nc))
                    check = 1
                    break
            if check: break
    for dead_enemy_r, dead_enemy_c in dead_enemy_position:
        field[dead_enemy_r][dead_enemy_c] = 0
    return len(dead_enemy_position)

def move_enemy(field: list) -> list:
    result = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n-1):
        result[i+1] = field[i]
    return result

def is_enemy(field:list):
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                return 0
    return 1

def start_game(field:list, archer_positions: list, D:int) -> int:
    # 모든 적들이 이동했다 -> 게임을 끝낸다.
    cnt = 0
    while not is_enemy(field):
        # 적을 공격한다. # 공격 받은 적을 센다. -> cnt에 더해준다.
        cnt += attack_enemy(field, archer_positions, D)

        # 적들을 이동시킨다.
        field = move_enemy(field)
    return cnt

if __name__ == "__main__":
    n, m, d = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(n))
    max_value = 0

    # 아처 포지션을 정해준다.
    for archer_cs in combinations(range(m), 3):
        archer_positions = list()

        # archer position 규격화
        for archer_c in archer_cs:
            archer_positions.append((n, archer_c))

        # 원본 arr가 손상되지 않도록, arr의 data를 복제한 field 생성
        field = deepcopy(arr)

        # field에서 game 시작
        max_value = max(start_game(field, archer_positions, d),max_value)
    print(max_value)