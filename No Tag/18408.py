import sys
string = sys.stdin.readline().rstrip("\n").split(" ")
string = sorted(string)
print(string[1])