import sys
input = sys.stdin.readline

def get_length_LCS(sub1:str, sub2:str) -> int:

    # sub1이 sub2 알파벳 하나와 비교하며 나오는 length 저장 공간.
    temp = [0 for _ in range(len(sub1) + 1)]

    # sub1의 알파벳 전부를 sub2 알파벳 하나하나와 비교
    for s2 in sub2:
        cnt = 0
        for idx, s1 in enumerate(sub1,start = 1):
            if cnt < temp[idx]:
                cnt = temp[idx]
            elif s1 == s2:
                temp[idx] = cnt + 1
                    
    return max(temp)

print(get_length_LCS(input().rstrip('\n'), input().rstrip('\n')))
