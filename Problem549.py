import math
from sympy import factorint

"""
Really long execution time.
There is scope to reduce the complexity and run time 
for findNumberForPrimePower
Will do it in near future
"""

def findNumberForPrimePower(basePrime, power):
    """
    (bp^n-1)/(bp-1) <= p < (bp^(n+1)-1)/(bp-1)
    bp^n <= p*(bp-1)+1 < bp^(n+1)
    n = log(p*(bp-1)+1)/log(bp)
    """
    endValue = 0
    ceiling = int(math.log(power*(basePrime-1)+1)/math.log(basePrime))
    for r in range(ceiling-1, -1, -1):
        divisor = int(((basePrime**(r+1))-1)/(basePrime-1))
        quotient = power//divisor
        endValue += quotient*(basePrime**(r+1))
        power = power - quotient*divisor
    return endValue

def findS(n):
    factorDict = factorint(n)
    nums = [findNumberForPrimePower(k,v) for k,v in factorDict.items()]
    return max(nums)

def findSumofS(n):
    sum = 0
    for i in range(2, n+1):
        print(i)
        sum += findS(i)
    return sum

if __name__ == '__main__':
    print(findSumofS(100000000))

