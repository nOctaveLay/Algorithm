import sys
a,b,c = map(int,sys.stdin.readline().split())
def mul(a,b):
    if b == 1: return a % c
    half = mul(a, b//2)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c
        
print(mul(a,b))