import sys

input=sys.stdin.readline

t = int(input())

'''
쿼터 = 25 센트
다임 = 10 센트
니켈 = 5 센트
페니 = 1 센트
'''


for _ in range(t):
    input_coin = int(input())
    result = [0] * 4
    
    # 쿼터 먼저 거슬러줌
    result[0] = input_coin // 25

    # 쿼터로 거슬러주고 남은 금액을 다임으로 거슬러줌
    input_coin %= 25
    result[1] = input_coin // 10

    # 다임으로 거슬러주고 남은 금액을 니켈로 거슬러줌
    input_coin %= 10
    result[2] = input_coin // 5

    # 니켈로 거슬러주고 남은 금액을 페니로 거슬러줌
    result[3] = input_coin % 5

    print(*result)