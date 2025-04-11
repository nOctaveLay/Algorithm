import sys
input=sys.stdin.readline

sentence = input().rstrip()

# 첫 단어는 무조건 1 이상이어야 하므로
# index는 1 이상부터 세야 한다.
result = ''
for spliter_i in range(1,len(sentence)-1):
    for spliter_j in range(spliter_i+1, len(sentence)):
        first_word = ''.join(reversed(sentence[:spliter_i]))
        second_word = ''.join(reversed(sentence[spliter_i:spliter_j]))
        third_word = ''.join(reversed(sentence[spliter_j:]))

        final_word = first_word + second_word + third_word

        result = sorted([result,final_word])[0] if result != '' else final_word

print(result)