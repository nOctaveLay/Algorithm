import sys
input = sys.stdin.readline

sentences = input().rstrip("\n")
result = ''
for word in sentences:
    for c in word:
        if c.isalpha():
            if c.isupper():
                basic_word = 'A'
            else:
                basic_word = 'a'
            result += chr(((ord(c)-ord(basic_word) + 13) % 26) + ord(basic_word))
        else:
            result += c
print(result,end ='')