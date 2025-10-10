import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().rstrip())

for c in arr:
    if 'a' <= c <= 'z':
        print(chr((ord(c)-ord('a')-k+26)%26+ord('a')), end='')
        k += 1
        if k == 26 : k = 1
    else:
        print(c,end='')
