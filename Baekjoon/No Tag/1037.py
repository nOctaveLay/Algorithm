import sys
num = int(sys.stdin.readline())
divisor_list = sys.stdin.readline().rstrip("\n").split(" ")
divisor_list = [int(x) for x in divisor_list]
divisor_list = sorted(divisor_list)
print(divisor_list[0] * divisor_list[-1])