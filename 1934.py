
def euclid_LCM(real_a,real_b):
    a = int(real_a)
    b = int(real_b)
    while b != 0:
        n = a%b
        a = b
        b = n
    gcd = a
    return gcd

iter_num = int(input())
for _ in range(iter_num):
    gcd_sum = 0
    input_string = input()
    input_list = input_string.split(" ")
    input_list = input_list[1:]
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            gcd_sum += euclid_LCM(input_list[i],input_list[j])
    print(gcd_sum)