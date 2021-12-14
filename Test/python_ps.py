import sys, subprocess
input = sys.stdin.readline
file_name = '9093.py'
with open('input.txt','r') as myinput, open('code_output.txt','w') as myoutput:
    subprocess.run(['python',file_name],stdin = myinput,stdout = myoutput)

with open('code_output.txt','r') as code_output, open('output.txt','r') as real_output:
    a = code_output.read()
    b = real_output.read()
    count = 0
    for i,j in zip(a,b):
        if i != j: 
            print('diff:',i,j) 
            count += 1
    if count == 0:
        print("finish")