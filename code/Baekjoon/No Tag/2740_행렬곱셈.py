import sys

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

N,a_M = sys.stdin.readline().rstrip("\n").split(" ")
N,a_M = int(N),int(a_M)
matrix_a = [sys.stdin.readline().rstrip("\n").split(" ") for _ in range(N)]
M,K = sys.stdin.readline().rstrip("\n").split(" ")
M,K = int(M),int(K)
matrix_b = [sys.stdin.readline().rstrip("\n").split(" ") for _ in range(M)]

ans = mul_matrix(matrix_a,matrix_b)
for row in ans:
	answer_string = ''
	for column in row:
		answer_string += f'{column} '
	answer_string = f'{answer_string[:-1]}\n'
	sys.stdout.write(answer_string)