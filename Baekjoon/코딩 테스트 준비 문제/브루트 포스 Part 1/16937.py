
import sys
input = sys.stdin.readline

def check(s1_r, s1_c, s2_r, s2_c):
    answer = 0
    square_sum = s1_r * s1_c + s2_r * s2_c
    if s1_r + s2_r <= h and max(s1_c,s2_c) <= w:
        answer = max(square_sum, answer)    
    if max(s1_r, s2_r) <= h and s1_c + s2_c <= w:
        answer = max(square_sum, answer)
    return answer

def return_max_square(stickers:list):
    answer = 0
    for i in range(n):
        s1_r,s1_c = stickers[i]
        for j in range(i+1,n):
            s2_r, s2_c = stickers[j]
            # 회전 x
            answer = max(answer,check(s1_r, s1_c, s2_r, s2_c))
            # s1 회전
            answer = max(answer,check(s1_c, s1_r, s2_r, s2_c))
            # s2 회전
            answer = max(answer,check(s1_r, s1_c, s2_c, s2_r))
            answer = max(answer,check(s1_c, s1_r, s2_c, s2_r))
        
    return answer

if __name__ == "__main__":
    h, w = map(int,input().split())
    n = int(input())
    stickers = list(tuple(map(int,input().split())) for _ in range(n))

    print(return_max_square(stickers))