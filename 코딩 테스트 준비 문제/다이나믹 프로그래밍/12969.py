def solve(length: int, a: int, b: int, lk: int) -> None:

    # 종료조건
    if length == n:
        if lk == k: # 조건 성립
            return True
        else:
            return False
    
    # dfs 조건
    if dp[length][a][b][lk]: return False # 기존에 방문했다면 -> 재 방문할 필요 없음.
    dp[length][a][b][lk] = True # 방문을 아직 안 했다면 -> 방문한 것으로 바꿔줌

    # 차례차례 A,B,C 넣어보기
    s[length] = 'A'

    # 'A' 는 S의 어떤 문자보다 작기 때문에, S[i] < S[j] 중 그 어느 수도 만족x
    if solve(length + 1, a+1, b, lk): return True 

    s[length] = 'B'
    # 'B' 는 S에서 'A'보다 크기 때문에, 'A'의 갯수가 S[i] < S[j] 를 만족시키는 수이다.
    if solve(length + 1, a, b+1, lk+a): return True

    s[length] = 'C'
    if solve(length + 1, a, b, lk + a + b): return True

    return False

if __name__ == "__main__":
    n, k = map(int,input().split())
    dp = [[[[0 for _ in range((n*(n-1)) // 2)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    s = ['' for _ in range(n)]
    if solve(0,0,0,0): print(*s,sep = '')
    else: print("-1")