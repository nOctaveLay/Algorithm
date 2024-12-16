n=int(input())
for i in range(1,n+1):
    if i == n:
        print(0)
        break
    sum_split = i
    for j in str(i):
        sum_split += int(j)
    if sum_split == n:
        print(i)
        break