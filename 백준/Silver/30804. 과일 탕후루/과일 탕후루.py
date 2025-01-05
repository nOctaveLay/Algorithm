import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

num_of_fruit = {}
left = 0
max_len = 0
for right in range(n):
    current_fruit = arr[right]
    
    if current_fruit not in num_of_fruit:
        num_of_fruit[current_fruit] = 1
    else:
        num_of_fruit[current_fruit] += 1

    while len(num_of_fruit) > 2:
        remove_fruit = arr[left]
        num_of_fruit[remove_fruit] -= 1
        if num_of_fruit[remove_fruit] == 0:
            del num_of_fruit[remove_fruit]
        left += 1
    max_len = max(max_len, right-left+1)
print(max_len)