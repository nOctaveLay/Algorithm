import sys
input=sys.stdin.readline
sum_value = 0
while True:
    try:
        a = int(input())
        sum_value += a
    except:
        break
print(sum_value)