# playlist_ songs: 플레이리스트에 있는 곡들
# different_songs : 플레이리스트에서 들었던 곡이나, 전부 다른 곡들
def solution(playlist_songs:int, different_songs:int) -> int:
    
    # 종료조건
    if playlist_songs == p:
        # 모든 곡을 다 들었을 경우 -> 이 경우를 count 한다.
        if n - different_songs == 0:
            return 1
        # 그렇지 않을 경우, 카운트 하지 않는다.
        else:
            return 0

    # 메모이제이션
    if dp[playlist_songs][different_songs] != -1: return dp[playlist_songs][different_songs]

    temp = 0
    
    # 루프 조건
    # 1. 만약 모든 곡을 다 듣지 않았을 경우 -> 일단 모든 곡을 다 듣게 만든다.
    if n - different_songs > 0: 
        temp += solution(playlist_songs + 1, different_songs + 1) * (n-different_songs)
    # 2. 모든 곡을 다 들었음에도, 곡이 넘친다면 -> 이전에 선택된 곡을 듣는 것이다.
    if different_songs - m > 0 :
        temp += solution(playlist_songs + 1, different_songs) * (different_songs - m)

    temp %= 1000000007
    dp[playlist_songs][different_songs] = temp
    return temp


if __name__ == "__main__":
    n, m, p = map(int,input().split())
    dp = [[-1 for _ in range(101)] for _ in range(101)]
    print(solution(0,0))