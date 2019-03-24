import math

max_allowed = 10000
min_allowed = 5
def calculate():
    highf = lambda n: n*(((n+1)/n)**(n+1))
    lowf = lambda n: n*((n/(n-1))**(n-1))
    i = 2
    sum_of_d = 0
    while True:
        l, h = lowf(i), highf(i)
        sum_of_d += sumup(i, l, h )
        i += 1
        if h > max_allowed:
            break
    print(sum_of_d)
        

def positive_if_recursive(numerator, denominator):
    gcd1 = math.gcd(numerator, denominator)
    numerator, denominator = numerator/gcd1, denominator/gcd1
    while denominator%2 == 0:
        denominator /= 2
    while denominator%5 == 0:
        denominator /= 5
    return 1 if denominator > 1 else -1
    
def sumup(i, low, high):
    low_int = int(math.ceil(low))
    high_int = int(math.floor(high))
    high_int = min(high_int, max_allowed)
    low_int = max(5, low_int)
    oursum = sum([positive_if_recursive(x, i)*x for x in range(low_int, high_int+1)])
    return oursum

if __name__ == '__main__':
    calculate()