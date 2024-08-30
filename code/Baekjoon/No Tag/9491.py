import sys
iter_num = int(sys.stdin.readline())

def fisano_period(M:int):
    k = M ** 2 - 1
    a,b,n = 1,2,1
    while a != 1 or b != 1:
        a,b = b % M,(a+b) % M
        n += 1
    return n
    
for _ in range(iter_num):
    P,M = sys.stdin.readline().strip().split(" ")
    P,M = int(P),int(M)
    answer = fisano_period(M)
    sys.stdout.write(f'{P} {answer}\n')