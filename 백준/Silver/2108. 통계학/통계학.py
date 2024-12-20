from collections import Counter
n=int(input())
arr = list(int(input()) for _ in range(n))
print(round(sum(arr)/n))
arr.sort()
print(arr[n//2])
max_count = 0
max_num = []
count = Counter(arr)
max_value = max(count.values())
max_int = list()
for key,value in count.items():
    if value == max_value:
        max_int.append(key)
max_int.sort()
if len(max_int) > 1:
    print(max_int[1])
else:
    print(max_int[0])
print(arr[-1]- arr[0])