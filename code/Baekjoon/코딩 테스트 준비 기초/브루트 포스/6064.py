import sys
input = sys.stdin.readline

# Extended Euclidean Algorithm
def EEA(a,b):
    s0,s1 = 1,0
    t0,t1 = 0,1
    r0,r1 = a,b
    while r1 > 0 :
        q = r0//r1
        r0, r1 = r1, -r1*q + r0
        s0, s1 = s1, -s1*q + s0
        t0, t1 = t1, -t1*q + t0
    return (r0,s0,t0)

if __name__ == "__main__":
    M,N,x,y = map(int,input().split())
    g,k0,_ = EEA(M,N)
    if (y-x) % g: 
        print(-1)
    else:
        k0 *= (y-x) // g
        k = M*k0 + x
        while k <= 0:
            k += (M * N) // g
        print(k)