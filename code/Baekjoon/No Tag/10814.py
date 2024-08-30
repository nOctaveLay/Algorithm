# 나이가 충분히 작고 (100 이하) non-negative integer이다
# 이를 보니 counting sort를 이용하면 되겠다.
import sys
input = sys.stdin.readline
n = int(input())
member_list = list()
max_num = 201

# counting sort (stable sort)
def CountingSort(input_list,k = max_num):

    count_list = [0]*k #나이를 세는 리스트
    output_list = [()]*n
    # first, count the num of keys
    for (age,name) in input_list:
        count_list[age] += 1
    # second, accumulate the count_list
    for i in range(1,len(count_list)):
        count_list[i] += count_list[i-1]
   
    # calculate
    for i in reversed(range(len(input_list))):
        age,name = input_list[i]
        output_list[count_list[age]-1] = (age,name) 
        count_list[age] -= 1
    return output_list
        

for i in range(n):
    age,name = input().rstrip("\n").split()
    member_list.append((int(age),name))

member_list = CountingSort(member_list)
for age,name in member_list:
    print(age, name)