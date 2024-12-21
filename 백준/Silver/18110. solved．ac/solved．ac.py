n=int(input())
def round(n):
    float_point = n - int(n)
    if float_point >= 0.5: return int(n) + 1
    else: return int(n)
if n==0:print(0)
else:
    arr=list(int(input()) for _ in range(n))
    arr=sorted(arr)
    cut_n=round(n*0.15)
    if cut_n != 0: arr = arr[cut_n:-cut_n] 
    print(round(sum(arr)/(n-cut_n*2)))