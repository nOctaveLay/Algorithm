import sys

def return_maximum_score():
    total_sum = 0
    for i in range(1 << (m*n)): #가로 표시를 0으로, 세로 표시를 1로 한다고 하자.

        # 가로로 표시된 애들을 모두 더해줌
        row_sum = 0
        for row in range(n):            
            temp_sum = 0
            for column in range(m):
                idx = row * m + column
                # 이 때 1과 같다고 해주기 위해선 그냥 1이 아니라 0b1이어야 한다. 주의!!
                if i & (1 << idx) != 0: 
                    temp_sum = temp_sum * 10 + arr[row][column]
                    
                else:
                    row_sum += temp_sum
                    temp_sum = 0
                    
            row_sum += temp_sum
                
        # 세로로 표시된 애들을 모두 더해줌
        column_sum = 0
        for column in range(m):
            temp_sum = 0
            for row in range(n):
                idx = row * m + column

                if i & (1 << idx) == 0:
                    temp_sum = temp_sum * 10 + arr[row][column]
                else:
                    column_sum += temp_sum
                    temp_sum = 0
            column_sum += temp_sum
        total_sum = max(total_sum,row_sum + column_sum)
    return total_sum


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    arr = [list(map(int,input().rstrip("\n"))) for _ in range(n)]
    print(return_maximum_score())