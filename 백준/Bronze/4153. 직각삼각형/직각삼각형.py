a,b,c=sorted(list(map(int,input().split())))
while(a!=0 or b!=0 or c!=0):
    print("right" if a**2+b**2==c**2 else "wrong")
    a,b,c=sorted(list(map(int,input().split())))