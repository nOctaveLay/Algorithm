import sys

def return_prev_value(current_value:str)->str:
    if current_value == 'B':
        return 'J'
    elif current_value == 'O':
        return 'B'
    else:
        return 'O'

def solution(arr:list) -> int:
    dp = [max_value for _ in range(n)] #dp[i] = i까지 이동했을 때 최소 에너지량.
    dp[0] = 0 # 이동을 안하니까 에너지가 없죠?
    for i in range(1,n):
        prev = return_prev_value(arr[i])
        for j in range(i):
            if arr[j] == prev:
                k = i - j 
                dp[i] = min(dp[i], dp[j] + k*k)
    return dp[-1] if dp[-1] != max_value else -1

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    street = list(input().rstrip("\n"))
    max_value = 10**6 + 1
    print(solution(street))