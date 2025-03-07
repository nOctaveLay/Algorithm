import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

result = [0]*n

for index, num_of_left in enumerate(arr):
    zero_count = 0
    for position in range(n):
        # 왼쪽에 키 큰 사람의 조건을 만족할 경우
        if zero_count == num_of_left:
            if result[position] == 0:
                result[position] = index + 1
                break
            
        # 조건을 만족하지 못할 경우

        if result[position] == 0:
            zero_count += 1
    

print(*result)
