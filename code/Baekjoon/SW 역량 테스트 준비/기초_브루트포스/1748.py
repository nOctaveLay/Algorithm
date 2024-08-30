import sys
n = int(sys.stdin.readline())
digit = len(str(n))
answer = 0
for x in range(0,digit-1):
    answer += (9 * 10 ** x) * (x+1)
answer += (n - 10**(digit-1)+1) * digit
sys.stdout.write(str(answer))