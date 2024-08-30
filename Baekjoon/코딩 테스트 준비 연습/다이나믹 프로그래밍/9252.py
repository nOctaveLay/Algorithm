import sys
input = sys.stdin.readline

def get_length_LCS(sub1:str, sub2:str) -> int:

    # sub1이 sub2 알파벳 하나와 비교하며 나오는 length 저장 공간.
    temp = ['' for _ in range(len(sub1) + 1)]

    # sub1의 알파벳 전부를 sub2 알파벳 하나하나와 비교
    for s2 in sub2:
        temp_string = ''
        for idx, s1 in enumerate(sub1,start = 1):
            if len(temp_string) < len(temp[idx]):
                temp_string = temp[idx]
            elif s1 == s2:
                temp[idx] = temp_string + s1     
    max_length = 0
    max_value = ''
    for i in temp:
        if max_length < len(i):
            max_length = len(i)
            max_value = i
    return (max_length, max_value)
sub1, sub2 = input().rstrip('\n'), input().rstrip('\n')
max_length, max_value = get_length_LCS(sub1,sub2)
print(max_length)
print(max_value)
