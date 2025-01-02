import sys
input=sys.stdin.readline
n=int(input())

# 1 : 1(+8), 9(+8), 17(+8), ...
# 2 : 2(+6), 8(+2), 10(+6), 16(+2),18 #0 #2
# 3 : 3(+4), 7(+3), 11, 15,19 # 8-1 = 7 #3
# 4 : 4(+2), 6(+6), 12, 14,20 # 6 # 4
# 5 : 5(+8), 13(+8),21 # 5 

# 일단 1,5가 8의 배수의 나머지인건 알겠으니까, 8로 나눠보자
q = n // 8
r = n % 8

if r == 1: print(1)
elif r == 5: print(5)
elif r == 2 or r == 0: print(2)
elif r == 7 or r == 3: print(3)
elif r == 6 or r == 4: print(4)
