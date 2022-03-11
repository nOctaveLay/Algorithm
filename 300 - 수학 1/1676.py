import sys

input = sys.stdin.readline
n = int(input())

'''
1. 10의 배수가 몇 개 있는지 확인하는 문제.
2. 보통 2 ^ n * 5 ^ m 승으로 확인하는 걸로 알고 있는데.
3. 각 수마다 얼마나 있는 지 확인해야 하는 거 아닌가?
'''

num_two = 0
num_five = 0
for i in range(1,n+1):
    while True:
        if i == 0: break
        if i % 2 == 0:
            i //= 2
            num_two += 1
        elif i % 5 == 0 :
            i //= 5
            num_five +=1
        else:
            break
print(min(num_two,num_five),end = '')