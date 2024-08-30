# https://www.acmicpc.net/problem/16235
# 혼자 어렵게 푼 문제. dict써도 풀리긴 풀릴텐데
# 항상 뭔가 나갔다 들어왔다 하는 건 deque 써도 된다는 사실 >.O 기억하자구

import sys
input = sys.stdin.readline

def spring(tree_ages:dict, food_field:list):
# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
# 1. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
    dead_tree_positions = []
    next_foods = dict()
    for positions in tree_ages:
        # 각 포지션에 있는 나무들의 나이들 list를 오름차순으로 정렬한다.
        # 그러면, 맨 앞에 있는 나무가 제일 어린 나무가 될 것이다.
        position_ages = sorted(tree_ages[positions]) 
        # 양분을 먹을 수 있는지 없는지 확인한다.
        # 양분이 담겨있는 plant를 food_field라고 하자.
        # food_field의 positions에 담겨있는 양분을 food_field[positions[0]][positions[1]]라 하고,
        # 그 position에 심어져있는 나무가 필요로 하는 양분을 position_tree_food라고 하자.
        for tree_index, position_tree_food in enumerate(position_ages):
        
            if food_field[positions[0]][positions[1]] - position_tree_food >= 0: # 이러면 영양분을 충분히 먹을 수 있다는 뜻이므로
                # 나무가 영양분을 섭취한다.
                food_field[positions[0]][positions[1]] -= position_tree_food

                # 나무의 나이가 증가한다.
                # 나무는 반드시 tree_index로 색인해야 한다.
                position_ages[tree_index] += 1


            else: # 만약, 필드의 영양분이 부족해, 나무가 영양분을 먹지 못한다고 하자.
                # 그러면 나무에게 기다리고 있는 건 차디찬 죽음 뿐이다.
                # 만약, tree_index == 0일 때,
                # 나무의 나이들을 포지션별로 묶어 둔 tree_ages dictionary에서 바로 제거해버린다면, tree_ages가 변화하게 되므로
                # for문은 갈피를 잃어버리게 된다.
                # 따라서 그런건 나중에 제거해주도록 하자.
                if tree_index != 0:
                    # 그리고, 여름에 봄에 죽은 나무가 양분으로 변하게 되므로, 이를 미리 계산해 주는데
                    # 각각을 2로 나누어 소수점을 버리고 더하므로, sum으로 계산하는 것은 위험하다.
                    # 따라서 이를 summer method에서 계산해주자.
                    next_foods[positions] = position_ages[tree_index:]
                    # position_ages를 update 시키기 위한 수작.
                    position_ages = position_ages[:tree_index]
                else:
                    # 그러려면 이 나무가 어떤 포지션의 어떤 나무인지 표기해둬야한다.
                    dead_tree_positions.append(positions)
                    next_foods[positions] = position_ages
                    position_ages = []
                # 그리고 요 나무가 못 먹었다면, 이 나무 뒤의 나무들은 반드시 영양분을 먹을 수 없다.
                # (왜냐하면 나무들의 나이가 많으면 많을 수록, 많이 먹는데 이 뒤에 남은 나무들의 나이는 현 나무보다 많기 때문이다.)
                break
        # 각 position마다, tree_age를 update 시켜줘야 한다.
        tree_ages[positions] = position_ages
    # 모든 과정이 끝나고, 
    # 그 위치에 나무가 아예 없을경우, tree_ages dict에서 제거해준다.
    for dead_tree_position in dead_tree_positions:
        del tree_ages[dead_tree_position]
    return tree_ages, next_foods

def summer(dead_tree_ages: dict, food_field:list):
    # 죽은 나무가 없을 경우 -> 아무짓도 하지 않음. 그냥 food_field를 그대로 return,
    # 죽은 나무가 있을 경우 ---> 각각을 계산해준다.
    for dead_tree_position in dead_tree_ages:
        position_food = 0
        for dead_tree_age in dead_tree_ages[dead_tree_position]:
            position_food += dead_tree_age // 2
        food_field[dead_tree_position[0]][dead_tree_position[1]] += position_food
    return food_field

def fall(tree_ages: dict):
    # 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
    # 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
    # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

    # 주의해야 하는 것은, 바로 인접한 칸에 나무들을 생성시키면 for문이 꼬여버린다는 것이다.
    # 따라서, 나이가 5의 배수인 나무들이 있으면, 포지션과 나이가 5의 배수인 나무들을 세서 저장한 뒤, 나중에 update 해주어야 한다.
    generate = []
    for positions in tree_ages:
        for tree_age in tree_ages[positions]:
            if tree_age % 5 == 0:
                generate.append(positions)
    d = [(-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1)]

    for positions in generate:
        x, y = positions
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n): continue 
            nposition = (nx,ny)
            if nposition in tree_ages:
                tree_ages[nposition].append(1)
            else:
                tree_ages[nposition] = [1]
    return tree_ages

def winter(a:list, food_field:list):
    for i in range(n):
        for j in range(n):
            food_field[i][j] += a[i][j]
    return food_field

def count_tree(tree_ages:dict):
    count = 0
    for position in tree_ages:
        for tree in tree_ages[position]:
            count += 1
    return count

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    tree_ages = dict()
    food_field = [[5 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, tree_age = map(int,input().split())
        position = (x-1,y-1)
        if position not in tree_ages:
            tree_ages[position] = [tree_age]
        else:
            tree_ages[position].append(tree_age)
    for year in range(1,k+1):
        tree_ages, dead_tree_ages = spring(tree_ages, food_field)
        food_field = summer(dead_tree_ages,food_field)
        tree_ages = fall(tree_ages)
        food_field = winter(a, food_field)
    answer = count_tree(tree_ages)
    print(answer)