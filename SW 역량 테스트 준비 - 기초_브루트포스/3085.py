import sys

def eat_row_and_column(matrix):
    max_num = 0
    n = len(matrix)
    for i in range(n):
        candy_count_row  = 1
        candy_count_column = 1

        for j in range(1,n):
            if matrix[j-1][i] == matrix[j][i]:
                candy_count_row += 1
            else:
                candy_count_row = 1

            if matrix[i][j-1] == matrix[i][j]:
                candy_count_column += 1
            else:
                candy_count_column = 1

            max_count = max(candy_count_row,candy_count_column)
            if max_num < max_count:
                max_num = max_count
    return max_num


iter_num = int(sys.stdin.readline())
ans = [list(sys.stdin.readline().rstrip("\n")) for _ in range(iter_num)]
return_max = 0
for i in range(len(ans)):
    for j in range(len(ans)):
        # swap row
        if i+1 < len(ans):
            ans[i][j],ans[i+1][j] = ans[i+1][j],ans[i][j]
            swap_row_max = eat_row_and_column(ans)

            # swap back
            ans[i][j],ans[i+1][j] = ans[i+1][j],ans[i][j]

        if j+1 < len(ans):        
            # swap column
            ans[i][j],ans[i][j+1] = ans[i][j+1], ans[i][j]
            swap_column_max = eat_row_and_column(ans)

            # swap back
            ans[i][j],ans[i][j+1] = ans[i][j+1], ans[i][j]
        
        swap_max = swap_row_max if swap_row_max > swap_column_max else swap_column_max
        if return_max < swap_max:
            return_max = swap_max

sys.stdout.write(str(return_max))