from sys import stdin
from collections import defaultdict

word = stdin.readline().strip()
word = word.upper()

chardic = defaultdict(int)
for char in word:
    chardic[char] += 1

maxvalue = max(chardic.values())
maxchar = '?'

for k, v in chardic.items():
    if v == maxvalue:
        if maxchar != '?':
            print("?")
            exit()
        else:
            maxchar = k

print(maxchar)