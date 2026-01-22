import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = input().rstrip()
    string = string[0].capitalize()+string[1:]
    print(string)

    
