import sys

input = sys.stdin.readline

n = int(input())

people_map = [list(map(int,input().split())) for _ in range(n)]

def cal_people(x,y,d1,d2):
    people_per_area = [0] * 5 # 선거구 당 인원수
    area_map = [[0] * n for _ in range(n)] # 선거구 매핑 (5구역만)

    # 지역 매핑
    # 경계선을 5번구로 할당
    '''
    1번 경계선: (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    2번 경계선: (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    3번 경계선: (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    4번 경계선: (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    '''
    for i in range(d1+1):
        area_map[x+i][y-i] = 5 # 1번 경계선
        area_map[x+d2+i][y+d2-i] = 5 # 4번 경계선

    for i in range(d2+1):
        area_map[x+i][y+i] = 5 # 2번 경계선
        area_map[x+d1+i][y-d1+i] = 5 # 3번 경계선

    # 경계선 안 쪽을 5번 지역구로 할당
    # area_map에서 5번을 만난 뒤 다시 5번을 만날 때까지 5번 지역구로 할당 가능
    # 그 행에 5가 하나 밖에 없는 경우 제외.
    # 즉 범위는 row : x+1 ~ x + d1 + d2 -1 까지. col을 기준으로 탐색

    # 지역구 인원수 계산
    '''
    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y, 1번 경계선의 왼쪽 위
    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N, 2번 경계선의 오른쪽 위
    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2, 3번 경계선의 왼쪽 아래
    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N, 4번 경계선의 오른쪽 아래
    '''

    total = 0
    for i in range(n):
        total += sum(people_map[i])

    # 1번 선거구
    for i in range(x+d1):
        for j in range(y+1):
            if area_map[i][j] != 0: break
            people_per_area[0] += people_map[i][j]

    # 2번 선거구
    for i in range(x+d2+1):
        for j in range(n-1,y,-1):
            if area_map[i][j] != 0: break
            people_per_area[1] += people_map[i][j]

    # 3번 선거구
    for i in range(x+d1, n):
        for j in range(y-d1+d2):
            if area_map[i][j] != 0: break
            people_per_area[2] += people_map[i][j]

    # 4번 선거구
    for i in range(x + d2 +1, n):
        for j in range(n-1,y-d1+d2-1,-1):
            if area_map[i][j] != 0: break
            people_per_area[3] += people_map[i][j]
    people_per_area[4] = total-sum(people_per_area)
    return abs(max(people_per_area)-min(people_per_area))

# main
result = float('inf')
for x in range(0,n):
    for y in range(0,n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if x+d1+d2 < n and 0 <= y - d1 and y + d2 < n:
                    result = min(result, cal_people(x,y,d1,d2))

print(result)