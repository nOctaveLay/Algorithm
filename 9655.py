input_num = int(input())
q = input_num // 3
r = input_num % 3

print("CY") if (q + r) % 2 == 0 else print("SK")