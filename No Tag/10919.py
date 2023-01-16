import sys
def delivery(n:int, k:int, l:int, positions:list):
    if k == 0: # 자신이 지금 손에 쥐고 있는 모든 선물을 다 줬다는 의미
        # 처음으로 돌아온다.