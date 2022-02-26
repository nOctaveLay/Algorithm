# 행렬 제곱
from unittest import result

def identity(b):
    result_list = list()
    for i in range(b):
        j_list = list()
        for j in range(b):
            if i == j:
                j_list.append(1)
            else:
                j_list.append(0)
        result_list.append(j_list)
    return result_list

def pow_matrix(matrix_A,b):
    # Base Case
    if b == 0 : return identity(len(matrix_A))
    # Divide Case
    if b % 2 == 1 : return multiply_matrix(matrix_A,pow_matrix(matrix_A,b-1))
    else:
        half_matrix = pow_matrix(matrix_A,b//2)
        return multiply_matrix(half_matrix,half_matrix)

def multiply_matrix(matrix_A,matrix_B):
    # Base Case
    if len(matrix_A[0]) != len(matrix_B):
        return -1
    else:
        m,n,l = len(matrix_A),len(matrix_A[0]),len(matrix_B)
        result = [[0] * l for _ in range(m)]
        for i in range(m):
            for k in range(l):            
                for j in range(n):
                    result[i][k] += (matrix_A[i][j] * matrix_B[j][k]) % 1000
                result[i][k] %= 1000
        return result
                    
if __name__ == "__main__":
    n,b = map(int,input().split())
    matrix_a = [list(map(int,input().split())) for _ in range(n)]
    result = pow_matrix(matrix_a,b)
    for elem in result[:-1]:
        print(*elem,sep=' ',end="\n")
    print(*result[-1],sep=' ',end="")