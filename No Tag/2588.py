import sys

input = sys.stdin.readline
a = int(input().rstrip("\n"))
b = input().rstrip("\n")

third_answer = a * int(b[-1])
forth_answer = a * int(b[-2])
fifth_answer = a * int(b[-3])
answer = third_answer + forth_answer*10 + fifth_answer*100

print(third_answer)
print(forth_answer)
print(fifth_answer)
print(answer)