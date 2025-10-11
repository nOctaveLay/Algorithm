import sys

input = sys.stdin.readline

x= int(input())
x_string = 'UOS'
print(x_string[(x+2)%3])