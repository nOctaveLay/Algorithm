from sys import argv
from random import choices
from math import sqrt

def main(trials, samples):
    total = 0
    total2 = 0
    for _  in range(trials):
        x = pickPoint(samples)
        y = pickPoint(samples)
        # Triangle side length are all 1
        v =  [(z[0]-z[1])**2 for z in zip(x,y)]
        d = sqrt(sum(v)/2)  # Euclidean distance
        total += d
        total2 += d*d
    mean = total/trials
    variance = total2/trials - mean**2
    print(variance)
    sigma = sqrt(variance/trials)
    return mean, sigma
    
def pickPoint(samples):
    V = [(1,0,0), (0,1,0), (0,0,1)]
    s = choices(range(3), k=samples)
    for k in s:
        v = V[k]
        V = [tuple((z[0]+z[1])/2 for z in zip(v,V[k])) for k in range(3)]  
    return [(V[0][k]+V[1][k]+V[2][k])/3 for k in range(3)]
    
if __name__ == '__main__':
    trials = 1000000
    samples = 30
    mu, sigma = main(trials, samples)
    print(f'Mean = {mu}')
    print(f'sigma = {sigma}')
    print(f'{trials} trials')
    print(f'Sample depth = {samples}')
    delta = 2.576*sigma
    print(f'99% confidence interval: ({mu-delta}, {mu+delta})')