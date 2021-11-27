# 피보나치수, 제일 빠른 방법
import sys
from collections import deque
input_num = int(sys.stdin.readline())
fib_matrix = [[1,1],[1,0]]

def mul_matrix(matrix1,matrix2):
	answer = [[0 for y in range(len(matrix2[0]))] for x in range(len(matrix1))]
	# 만약 matrix1의 열의 갯수와 matrix2의 행의 갯수가 같지 않다면 행렬의 곱이 불가능하다.
	if len(matrix1[0]) != len(matrix2):
		return -1
	else:
		for i in range(len(answer)): #행
			for j in range(len(answer[0])): #열
				for k in range(len(matrix1[0])): # matrix1의 열 = matrix1의 element
					answer[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
		return answer

if input_num % 2 != 0 :
	remainer = fib_matrix
else:
	remainer = [[1,0],[0,1]] # 항등 행렬 E

answer = [[1,0],[0,1]]
base_matrix = fib_matrix
while input_num != 0:
	if input_num % 2 != 0:
		answer = mul_matrix(answer,base_matrix)
	input_num //= 2
	base_matrix = mul_matrix(base_matrix,base_matrix)

sys.stdout.write(str(answer[1][0] % 1000000))
