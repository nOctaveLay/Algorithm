import sys

input = sys.stdin.readline

a = sum(int(input()) for _ in range(4))
print("Yes" if a + 300 <= 1800 else "No")