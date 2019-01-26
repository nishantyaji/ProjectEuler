import math

# A = i +(b/2) -1, Picks Theorem

def findNumBoundaryPoints(a,b,c,d):
    gcdab = findGCD(b,a)
    gcdbc = findGCD(b,c)
    gcdcd = findGCD(c,d)
    gcdda = findGCD(d,a)
    return gcdab+gcdbc+gcdcd+gcdda

def findGCD(x, y):
    x,y = abs(x), abs(y)
    gcdxy = math.gcd(x, y)
    return gcdxy

def is_square(n):
    f = math.sqrt(n)
    i = int(f)
    return i*i == n

def calculate(m):
    result = 0
    for a in range(1, m+1):
        for b in range(1,m+1):
            for c in range(1,m+1):
                for d in range(1,m+1):
                    A = ((a*b)/2)+((b*c)/2)+((c*d)/2)+((d*a)/2)
                    bp = findNumBoundaryPoints(a,b,c,d)
                    i = A-(bp/2)+1
                    if is_square(i):
                        result += 1
    return result


if __name__ == '__main__':
    print("->",calculate(100))