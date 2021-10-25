import sys
a1,a2,a3 = sys.stdin.readline().rstrip("/n").split(" ")
a1,a2,a3 = int(a1)-1,int(a2)-1,int(a3)-1

# 중국인의 나머지 정리를 이용하여 a1,a2,a3가 나오게 하면 된다.

# 식의 설계

mod1,mod2,mod3 = 15, 28, 19

n = mod1 * mod2 * mod3

n1 = n // mod1
n2 = n // mod2
n3 = n // mod3

x1 = 0
x2 = 0
x3 = 0

x1_true = 0
x2_true = 0
x3_true = 0

# 선형 합동식 특수해
while True:
    if (n1 * x1) % mod1 != 1 and x1_true != 1:
        x1 += 1
    else :
        x1_true = 1

    if (n2 * x2) % mod2 != 1 and x2_true != 1:
        x2 += 1
    else : x2_true = 1

    if (n3 * x3) % mod3 != 1 and x3_true != 1:
        x3 += 1
    else: x3_true = 1
    
    if x1_true == 1 and x2_true == 1 and x3_true == 1:
        break

result = a1*x1*n1+ a2*x2*n2 + a3*x3*n3
print(result % n + 1)