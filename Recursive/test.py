import random
n = 20
with open("./answer.txt","w") as f:
    for i in range(n):
        for j in range(n-1):
            if i != j:
                a = random.randrange(0,100)
            else:
                a = 0
            f.write(str(a)+ " ")
        if i == n:
            a = 0
        else:
            a = random.randrange(0,100)
        f.write(str(a)+"\n")