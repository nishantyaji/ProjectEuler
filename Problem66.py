from math import sqrt

def isSquare(number):
    sqrtInt = int(sqrt(number))
    return (number == sqrtInt * sqrtInt)

def pellSolution(number):
    x = 2
    while(True):
        ysq = (x*x - 1)/number
        if(isSquare(ysq) == True):
            print(number, "(", x, ",", int(sqrt(ysq)), ")")
            return(x)
        else:
            x += 1

max = 0
for i in range(2,1000,1):
    if(isSquare(i) == False):
        x = pellSolution(i)
        if(x > max):
            max = x

print(max)
