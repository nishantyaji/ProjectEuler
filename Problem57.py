from math import log as logarithm
from math import floor
from array import *

def moredigits(a, b):
    loga, logb = logarithm(a,10), logarithm(b,10)
    loga, logb = floor(loga), floor(logb)
    return loga > logb
    

list = [(3,2)]
newlist = []

for index in range(2, 1000):
    num,den = list[len(list)-1][0]+ 2*list[len(list)-1][1], list[len(list)-1][0]+list[len(list)-1][1]
    list.append((num,den))
    if(moredigits(num,den)):
        newlist.append((num,den))

print(len(newlist))