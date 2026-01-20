import sys

input = sys.stdin.readline


def decode(o_text):
    code_text = ['000000','001111','010011','011100','100110','101001','110101','111010']
    d_text = ''
    for code_i, code in enumerate(code_text):
        if code == o_text:
            return chr(ord('A')+code_i)
        else:
            count = 0
            for i in range(6):
                if o_text[i] != code[i]:
                    count += 1
            if count == 1:
                return chr(ord('A')+code_i)
    return -1

n = int(input())

cyper_text = input().rstrip()
answer = ''
for i in range(n):
    decode_text = decode(cyper_text[i*6:i*6+6])
    if decode_text == -1:
        print(i+1)
        exit()
    else:
        answer += decode_text
print(answer)
    