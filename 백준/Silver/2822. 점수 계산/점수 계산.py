import sys

input = sys.stdin.readline
arr = []
for i in range(8):
    arr.append((i+1, int(input())))

arr = sorted(arr,key=lambda x:x[1],reverse=True)
answer_sum = 0
problem_number = []
for i in range(5):
    answer_sum += arr[i][1]
    problem_number.append(arr[i][0])
print(answer_sum)
print(*sorted(problem_number))