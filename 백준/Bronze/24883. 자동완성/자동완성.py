import sys

input = sys.stdin.readline

input_string = input().rstrip()
if input_string == 'N' or input_string == 'n':
    print("Naver D2")
else:
    print("Naver Whale")