n=int(input())
size_arr=list(map(int,input().split()))
t,p=map(int,input().split())
total_tshirt = 0
for num_size in size_arr:
    num_group = num_size // t
    if num_size % t != 0: num_group += 1
    total_tshirt += num_group
print(total_tshirt)
print(n//p, n%p)