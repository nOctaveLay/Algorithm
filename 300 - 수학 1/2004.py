'''
1. 이 문제는 팩토리얼의 소인수 분해한 제곱수들이 어떻게 생겼는지 알기만 하면 끝난다.
2. 이 문제는 아직 이르다 -> 정수론을 제대로 공부하고 나서 할 것.
'''

import sys
input = sys.stdin.readline
n,m = map(int,input().split())



def divide_num(n,m=2):
    result = 0
    while True:
        if n == 0 : break
        n //= m
        result += n
    return result

a1 = divide_num(n,2)
a2 = divide_num(m,2)
a3 = divide_num(n-m,2)
two_result = a1 - a2 - a3

a1 = divide_num(n,5)
a2 = divide_num(m,5)
a3 = divide_num(n-m,5)
five_result = a1 - a2 - a3


print(min(two_result,five_result),end = '')