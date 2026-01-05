import sys

input = sys.stdin.readline

def check_msg(check_string):
    seq_consonant_count = 0
    seq_vowel_count = 0
    vowel_count = 0
    success_msg = f"<{check_string}> is acceptable."
    fail_msg = f"<{check_string}> is not acceptable."


    for c in range(len(check_string)):
        # 모음이라면
        if check_string[c] in ['a','e','o','i','u']:
            vowel_count += 1
            if seq_vowel_count == 0:
                seq_consonant_count = 0 
            seq_vowel_count += 1
        else: # 자음이라면
            if seq_consonant_count == 0 : # 이전의 문자가 자음이 아니라면
                seq_vowel_count = 0 #현 문자가 모음이 아니므로 연속성이 끊김
            seq_consonant_count += 1

        # 모음 3개 혹은 자음 3개 연속이면 exit
        if seq_vowel_count == 3 or seq_consonant_count == 3:
            return fail_msg
        
        # 같은 글자가 연속으로 두 번 올 경우 (ee, oo 제외)
        if c > 0 and check_string[c-1] == check_string[c]:
            if check_string[c] != 'e' and check_string[c] != 'o':
                return fail_msg


    # 모음 하나를 반드시 포함
    if not vowel_count:
        return fail_msg
    return success_msg    

while True:
    check_string = input().rstrip()
    if check_string == 'end': break
    print(check_msg(check_string))
