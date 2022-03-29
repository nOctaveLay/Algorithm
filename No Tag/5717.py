import sys
input = sys.stdin.readline
num_of_friends = sum(map(int,input().split()))
while num_of_friends != 0:
    print(num_of_friends)
    num_of_friends = sum(map(int,input().split()))
