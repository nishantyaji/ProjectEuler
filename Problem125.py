from math import floor

def squareSum(num):
    return int(num*(num+1)*(2*num+1)/6)

def isPalindrome(num):
    numString = str(num)
    mid = floor(len(numString)/2)
    for i in range(0, mid, 1):
        if(numString[i] != numString[len(numString) - 1 - i]):
            return False
    return(True)

s = set([])
maxLimit = 10000
for i in range(2, maxLimit, 1):
    for j in range(0, i-1, 1):
        diff = squareSum(i) - squareSum(j)
        if(diff < 100000000):
            if(isPalindrome(diff)):
                s.add(diff)
               
print(sum(s))