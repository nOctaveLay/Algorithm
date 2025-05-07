import sys

input=sys.stdin.readline

change = 1000 - int(input())

num_of_coin = 0
for coin in [500,100,50,10,5,1]:
    num_of_coin += change // coin
    change %= coin
print(num_of_coin, end='')