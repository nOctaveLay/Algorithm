import sys
n,m = sys.stdin.readline().split(" ")
n,m = int(n), int(m)
matrix = [sys.stdin.readline().rstrip("\n").split(" ") for _ in range(n)]
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y] = int(matrix[x][y])

# nm = 10**4이므로 이는 brute-force로 풀어도 됨을 의미한다.
# 단, Case가 굉장히 복잡하므로 미리 나눠서 풀려고 한다.
# 기준은 항상 왼쪽 위를 기준으로 하고, 따라서 종료조건은 각 block의 꼭지점이다.
result_sum = 0

# 1. 일자형
# 1-1 누어있는 일자형
    # 이는 행은 같고, 열은 1이다.
for i in range(n): # 행, 세로
    for j in range(m-3): # 열, 가로
        temp_sum = sum(matrix[i][j:j+4])
        result_sum = max(result_sum,temp_sum)

# 1-2 서 있는 일자형
for i in range(n-3): #행
    for j in range(m): #열
        temp_sum = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
        result_sum = max(result_sum,temp_sum)
 
# 2. L형
# 2-1. L 0도, 180도, L 반전 0도, L 반전 180도
for i in range(n-2): # 행
    for j in range(m-1): # 열

        # 0도와 L반전 180도는 한 숫자만 다르다
        temp_sum_zero = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j]
        diff_zero = matrix[i+2][j+1] if matrix[i+2][j+1] > matrix[i][j+1] else matrix[i][j+1]
        temp_sum = temp_sum_zero + diff_zero

        # 마찬가지로, 180도와 L반전 0도도 한 숫자만 다르다.
        temp_sum_one_eighty = matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1]
        diff_one_eighty = matrix[i+2][j] if matrix[i+2][j] > matrix[i][j] else matrix[i][j]
        temp_sum2 = temp_sum_one_eighty + diff_one_eighty

        result_sum = max(result_sum,temp_sum,temp_sum2)

# 2-2. L 90도, L 반전 270도
for i in range(1,n): # 행
    for j in range(m-2): # 열
        temp_sum_ninty = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
        diff_ninty = matrix[i-1][j+2] if matrix[i-1][j+2] > matrix[i-1][j] else matrix[i-1][j]
        temp_sum = temp_sum_ninty + diff_ninty
        
        result_sum = max(result_sum,temp_sum)

# 2-3. L 270도, L 반전 90도
for i in range(n-1): # 행, 세로
    for j in range(m-2): # 열, 가로
        temp_sum_two_seventy = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
        diff_two_seventy = matrix[i+1][j] if matrix[i+1][j] > matrix[i+1][j+2] else matrix[i+1][j+2]
        temp_sum = temp_sum_two_seventy + diff_two_seventy

        result_sum = max(result_sum,temp_sum)

# 3. 네모형 - 한 가지 케이스밖에 존재하지 않는다.
for i in range(n-1): #행, 세로
    for j in range(m-1): #열, 가로
        temp_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        result_sum = max(result_sum,temp_sum)
        
# 4. 번개형
for i in range(n-2): #행, 세로
    for j in range(m-1): #열, 가로
        
        # 4-1 번개 0도 = 번개 180도
        temp_sum_zero = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]

        # 4-3 번개 회전 0도
        temp_reverse_zero = matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j]

        result_sum = max(result_sum,temp_sum_zero,temp_reverse_zero)

for i in range(n-1):
    for j in range(m-2):

        # 4-2 번개 90도
        temp_sum_ninty = matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i][j+2]   

        # 4-4 번개 회전 90도
        temp_reverse_ninty = matrix[i][j] + matrix[i][j+1]+ matrix[i+1][j+1] + matrix[i+1][j+2]
        
        result_sum = max(result_sum,temp_sum_ninty,temp_reverse_ninty)

# 5. ㅜ형
for i in range(n-1): #행, 세로
    for j in range(m-2):
        # 5-1 ㅜ
        temp_sum_zero = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]

        # 5-3 ㅗ
        temp_sum_eighty = matrix[i+1][j] + matrix[i+1][j+1] + matrix[i][j+1] + matrix[i+1][j+2]

        result_sum = max(result_sum,temp_sum_zero,temp_sum_eighty)

for i in range(n-2):
    for j in range(m-1):

        # 5-2 ㅏ
        temp_sum_ninty = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j]

        # 5-4 ㅓ
        temp_sum_two_seventy = matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1] +matrix[i+2][j+1]

        result_sum = max(result_sum,temp_sum_ninty, temp_sum_two_seventy)

print(result_sum)