import sys
input=sys.stdin.readline

# 소수 판정
prime_table = [True] * 1000001

m = int(1000001**0.5)

# 소수 아닌 초기값
prime_table[0] = False
prime_table[1] = False

for i in range(2,m+1):
  if prime_table[i]:
    for k in range(i+i,1000001,i):
      prime_table[k] = False

while True:
  n = int(input())
  if n==0: break
  else:
    conjecture = 0
    for i in range(2,m+3):
      if prime_table[i] and prime_table[n-i]:
        print("%d = %d + %d"%(n,i,n-i))        
        conjecture = 1
        break
    if conjecture == 0: print("Goldbach's conjecture is wrong.")