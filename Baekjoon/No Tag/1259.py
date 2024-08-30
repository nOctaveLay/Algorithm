#펠린드롬

import sys

def fel(n):
    str_n = str(n)
    for i in range(len(str_n)//2):
        if str_n[i] != str_n[len(str_n)-i-1]:
            return 0
    return 1

while True:
    n = int(sys.stdin.readline())
    if n == 0 : break
    else:
        if fel(n) : sys.stdout.write('yes\n')
        else: sys.stdout.write('no\n')