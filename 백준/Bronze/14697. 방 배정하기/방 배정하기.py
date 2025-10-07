import sys

input=sys.stdin.readline

A,B,C,N = map(int,input().split())

def check_all():
    for a in range(N//A+1):
        for b in range(N//B+1):
            for c in range(N//C+1):
                if a*A + b*B + c*C == N:
                    return 1
    return 0

print(check_all())