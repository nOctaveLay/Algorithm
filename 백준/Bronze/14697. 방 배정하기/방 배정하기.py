import sys

input=sys.stdin.readline

A,B,C,N = map(int,input().split())

def check_all():
    for a in range(A):
        for b in range(B):
            for c in range(C):
                if a*A + b*B + c*C == N:
                    return 1
    return 0

print(check_all())