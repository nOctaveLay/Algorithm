from itertools import combinations
import sys
input = sys.stdin.readline


# 1. anta, tica도 배워야 함 => a,c,i,t,n 총 5개
# 2. 모든 단어는 anta로 시작해 tica로 끝나므로, 5개 이하로 알파벳을 배우는 경우 뒤에 관계없이 무조건 0
# 2. 그렇지만 anta, tica만으로 만들어질 수 있는 단어는 배울 수 있으므로, 이 점에 주의해야 함-> antatica,antatatica

def dfs(idx, cnt):
    global result
    global visited
    if cnt == k - 5:
        # 단어들을 센다
        word_cnt = 0
        for word in words:
            check = True
            for c in word:
                if visited & (1 << (ord(c) - ord('a'))): continue
                else:
                    check = False 
                    break
            if check: word_cnt += 1
        result = max(result, word_cnt)
        return
    for i in range(idx,26):
        if not visited & (1 << i):
            visited |= 1 << i
            dfs(i,cnt+1)
            visited ^= (1 << i)

if __name__ == "__main__":
    n, k = map(int,input().split())
    result = 0
    if k < 5: print(result) # anta, tica를 못배우는 경우
    elif k == 26 : print(n) # 알파벳을 다 배울 수 있으면 모든 문장을 읽을 수 있음
    else:
        basic_list = ['a','c','i','t','n']
        visited = 0
        for c in basic_list:
            # 방문했다는 것을 알려야 함
            visited |= 1 << (ord(c) - ord('a'))

        words = [set(input().rstrip("\n")) for _ in range(n)]
        dfs(0,0)
        print(result)
                            
            