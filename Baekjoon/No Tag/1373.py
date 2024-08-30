import sys
a = format(int('0b'+sys.stdin.readline().rstrip("\n"),2),'o')
print(a,end='')
