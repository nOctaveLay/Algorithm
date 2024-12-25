t=int(input())

# 1 <= N <= 100 and P(N)?
# overhead arr[0]. but it is resonably small.

arr=[0 for _ in range(101)] 

# init arr
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

# make left thing
for i in range(6,len(arr)):
    arr[i] = arr[i-1] + arr[i-5]
# calculate
for _ in range(t):
    n=int(input())
    print(arr[n])