import sys
input = sys.stdin.readline
output= sys.stdout.write

a,b,c,d = map(int,input().split())

sum_a_b = str(a)+str(b)
sum_c_d = str(c)+ str(d)
output(str(int(sum_a_b) + int(sum_c_d)))