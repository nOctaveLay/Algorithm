
# 행렬 제곱
# n의 크기를 갖는 항등 행렬을 return 한다.
def identity(n):
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]

# matrix끼리의 곱을 구해서 return해준다.
def multiply_matrix_mod_1000(matrix1,matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1))) % 1000 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

# (matrix)^b을 구한다.
def pow_matrix(matrix,b):

    # Base Case
    if b == 0 : return identity(len(matrix))

    # Divide Case
    if b % 2 == 1 : return multiply_matrix_mod_1000(matrix,pow_matrix(matrix,b-1))
    else:
        half_matrix = pow_matrix(matrix,b//2)
        return multiply_matrix_mod_1000(half_matrix,half_matrix)
                    
if __name__ == "__main__":    
    import sys
    input = sys.stdin.readline
    n,b = map(int,input().split())
    matrix_a = [list(map(int,input().split())) for _ in range(n)]
    result = pow_matrix(matrix_a,b)
    for elem in result[:-1]:
        print(*elem,sep=' ',end="\n")
    print(*result[-1],sep=' ',end="")