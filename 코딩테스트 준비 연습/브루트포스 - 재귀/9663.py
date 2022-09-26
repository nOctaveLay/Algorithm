import sys
input = sys.stdin.readline

def promising(x):
    for i in range(x):
        # quuen[x] == queen[i] 려면 무조건 promising에 들어온 column값과, x 이전에 들어온 아이들의 column 값이 된다는 의미므로 queen을 놓을 수 없다.
        # abs(queen[x] - queen[i]) == abs(x-i) : 대각선이 같다는 의미이다.
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x-i):
            return False
    return True

def n_queen(row):
    global answer
    if row == n:
        answer += 1
        return
    for column in range(n):
        queen[row] = column 
        if promising(row):
            n_queen(row + 1)

if __name__ == "__main__":
    n = int(input())
    answer = 0
    queen = [0 for _ in range(n)] # queen의 위치를 표현한 것이다. #queen[row] = queen이 들어가있는 그 row의 column 값이 나오게 되어있다.
    n_queen(0)
    print(answer)
