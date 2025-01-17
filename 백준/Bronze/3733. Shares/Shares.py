'''
문제 해석 : N명의 사람들로 이루어진 그룹과 심판 한명이 S개의 주식을 동등하게 나눠가진다.
각각의 사람들이 x개의 주식을 나눠가진다고 할 때, x의 최대값을 구하시오.

N과 S는 공백으로 구분되고, 파일은 EOF를 만나면 중단한다.

'''
import sys;sys.stdin.readline
while True:
    try:
        n,s=map(int,input().rstrip().split())
        x = s // (n+1)
        print(x)
    # EOF를 만나면 중단
    except EOFError: 
        break