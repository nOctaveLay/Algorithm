from itertools import combinations
import sys
import copy

def attack(arr:list, attacker_poses:list):

    # 궁수별 가까운 적 공격하기
    attack_list = list()
    cnt = 0
    for l in attacker_poses:
        pos = list()
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    now_d = abs(i - n) + abs(j - l)
                    if d >= now_d:
                        pos.append((now_d, i, j))
        
        pos.sort(key=(lambda x: (x[0], x[2]))) 
        if pos:
            attack_list.append(pos[0])   # 제거해야할 적

    for a in attack_list:
        _, i, j = a
        if temp[i][j] == 1:
            temp[i][j] = 0
            cnt += 1
    return cnt

def move():
    for i in range(-1, -n, -1):
        temp[i] = temp[i - 1]

    temp[0] = [0 for _ in range(m)]

def is_empty():
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True

if __name__ == "__main__":
    n, m, d = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    min_value = 0

    for attacker_poses in combinations(range(m), 3):
        temp = copy.deepcopy(arr)
        count = 0
        while not is_empty():
            count += attack(arr,list(attacker_poses))
            move()
        min_value = max(min_value, count)

    print(min_value)