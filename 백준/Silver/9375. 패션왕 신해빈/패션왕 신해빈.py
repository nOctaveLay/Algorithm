import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    clothes_dict = dict()
    for _ in range(n):
        v, k = input().rstrip().split()
        
        if k not in clothes_dict:
            clothes_dict[k] = 1
        else:
            clothes_dict[k] += 1
    result = 1
    for _, value in clothes_dict.items():
        result *= (value+1)
    print(result-1)