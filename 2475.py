import sys
vertification_list = [int(x) for x in sys.stdin.readline().rstrip("\n").split(" ")]
sum = 0
for x in vertification_list:
    sum += x ** 2
vertification_num = sum % 10
sys.stdout.write(str(vertification_num))