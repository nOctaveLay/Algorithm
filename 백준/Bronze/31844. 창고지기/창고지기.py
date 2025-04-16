storage = list(input())
robot = storage.index("@")	# 로봇의 위치
box = storage.index("#")	# 박스의 위치
flag = storage.index("!")	# 깃발의 위치

if (robot < box < flag) or (robot > box > flag):
    commandFirst = abs(box - robot) - 1
    commandSecond = abs(flag - box)
    print(commandFirst + commandSecond)
else:
    print(-1)
