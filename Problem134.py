from sympy import nextprime
from math import log10
from math import floor

def findModof10Power(index, prime):
    rem  = 1
    for _ in range(0, index, 1):
        rem = (rem * 10) % prime
    return rem

def findN(p1, p2):
    p1NumDigits = floor(log10(p1) + 1)
    rem = findModof10Power(p1NumDigits, p2)
    for a in range(1, p2, 1):
        if( (a*rem + p1) % p2 == 0 ):
            return a *(10**p1NumDigits) + p1
        
p1 = 5
maxp1 = 1000000
sum = 0
while(p1 < maxp1):
    p2 = nextprime(p1)
    sum += findN(p1, p2)
    p1 = p2

print(sum)