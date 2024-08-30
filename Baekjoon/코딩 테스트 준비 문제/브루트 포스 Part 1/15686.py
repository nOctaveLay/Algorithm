# Problem  : https://www.acmicpc.net/problem/15686
from itertools import combinations

def find_min_city_chicken_distance(chicken_houses:list, houses:list) -> int:

    min_chicken_distance = 1500

    # 치킨집 중에서 M개를 고른다.
    for select_chicken_houses in combinations(chicken_houses, m):
        min_city_distances = [1500 for _ in range(len(houses))]
        for chicken_house in select_chicken_houses:
            # 도시의 치킨 거리를 구한다.
            for house_idx, house in enumerate(houses):
                chicken_distance = abs(chicken_house[0] - house[0]) + abs(chicken_house[1] - house[1])
                min_city_distances[house_idx] = min(min_city_distances[house_idx], chicken_distance)

        # 만약 구한 도시의 치킨 거리 값이 기존의 도시의 치킨 거리 값과 비교했을 때 더 작다면
        # Update 한다. (치킨 거리 값의 최소를 구하는 문제이다.)
        city_distance = sum(min_city_distances)
        min_chicken_distance = min(city_distance, min_chicken_distance)
    return min_chicken_distance

if __name__ == "__main__" :
    n, m = map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(n))
    houses = list()
    chicken_houses = list()

    # house, chicken_house 좌표를 houses, chicken_houses에 저장한다.
    for i in range(n):
        for j in range(n):
            # 일반 집일때
            if arr[i][j] == 1: 
                houses.append((i,j))
            elif arr[i][j] == 2:
                chicken_houses.append((i,j))

    result = find_min_city_chicken_distance(chicken_houses, houses)
    print(result)