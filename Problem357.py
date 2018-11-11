from sympy.ntheory import factorint, isprime
from sympy import divisors

def satisfiesCondition(x):
    divs = divisors(x)
    for d in divs:
        n =  int(d + x / d)
        if( isprime(n) == False):
            return False
    return True

sum = 3
max = 10**8

for i in range(4, max+1, 2):
    factorization = factorint(i)
    filteredDict = {k: v for k, v in factorization.items() if v!= 1}
    if(len(filteredDict) == 0 ):
         if(satisfiesCondition(i)):
            print("-->",i)
            sum += i
        
print(sum)