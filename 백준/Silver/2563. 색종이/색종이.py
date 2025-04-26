import sys
input = sys.stdin.readline

"""
색종이를 붙인 위치는 두 개의 자연수로 구성됨.
흰색 도화지를 (1,1)을 원점으로 하는 좌표 평면으로 만든다고 가정하면
가로, 세로의 길이가 각각 100이므로 그 흰색 도화지의 끝은 (101, 101)일 것이다.
"""
plane = [[0] * 101 for _ in range(101)] # (0,0), (0,1), (1,0)은 쓰지 않지만, 편의를 위해 이렇게 작성한다.

"""
가로 10, 세로 10인 정사각형 셀로판지 이므로 이산적으로 계산해도 큰 문제가 없다.
검은색 셀로판지를 여러개 붙여 겹치는 부분을 빼는 과정 대신
검은색 셀로판지가 있는 지점에 좌표를 찍는 것으로 대체한다. 
"""

num_of_paper = int(input())
result = 0

for _ in range(num_of_paper):
    x, y = map(int,input().split())
    """
    plane은 y축부터 접근한다.
    x ~ x+9 까지 (총 10개) y ~ y+9 까지 (총 10개)
    range(a,b)는 a ~ b-1 까지 산출한다.
    """
    for p_y in range(y, y+10): 
        for p_x in range(x, x+10):
            if plane[p_y][p_x] != 1:
                plane[p_y][p_x] = 1
                result += 1
print(result)