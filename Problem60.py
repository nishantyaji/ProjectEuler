import sympy
import copy 
import time 
import sys

class MySet:
    def __init__(self, givenSet=None, limit=5):
        self.limit = limit
        if len(givenSet) > 0:
            self.internalSet = givenSet

    @staticmethod
    def isPrimeWhenJoined(num1, num2):
        numJoined1 = int(str(num1)+str(num2))
        numJoined2 = int(str(num2)+str(num1))
        return sympy.isprime(numJoined1) and sympy.isprime(numJoined2)

    def addIfEligible(self, num):
        eligible = True
        for elem in self.internalSet:
            if MySet.isPrimeWhenJoined(elem, num) == False:
                eligible = False
                break
        if eligible == True:
            self.internalSet.add(num)
            if len(self.internalSet) == self.limit:
                print('set:', self.internalSet, ',sum:', sum(self.internalSet))
                sys.exit(0)
        return eligible

    def deepcopy(self):
        setCopy = copy.deepcopy(set(sorted(self.internalSet)))
        return MySet(givenSet=setCopy)

class MyList:
    def __init__(self, givenSet=None):
        self.internalList = []
        if givenSet != None:
            self.internalList.append(givenSet)

    def addPrimeWhereverPossible(self, prime):
        for setElem in self.internalList:
            setCopy = setElem.deepcopy()
            if setCopy.addIfEligible(prime) == True:
                self.internalList.append(setCopy)
        self.internalList.append(MySet(givenSet={prime}))

def timeit(func):
    def inner(*args, **kwargs):
        starttime = time.time()
        func(*args, **kwargs)
        endtime = time.time()
        print('Total execution time is: ', endtime-starttime)
    return inner

@timeit
def calculate():
    listOfSets = MyList(MySet(givenSet={3}))
    prime = 5
    maxAllowed = 10**6
    while prime < maxAllowed:
        listOfSets.addPrimeWhereverPossible(prime)
        prime = sympy.nextprime(prime)
    
if __name__ == '__main__':
    calculate()