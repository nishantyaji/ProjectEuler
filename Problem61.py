import math

def figurate(ordinal, n):
    if n >= 3 or n <= 8:
        return n*(n+1+((ordinal-3)*(n-1)))/2
    else:
        raise Exception('You should not be here')

def appendToMap(ordToSeriesMap, ordinal, num):
    if ordinal in ordToSeriesMap:
        arr = ordToSeriesMap[ordinal]
        arr.append(num)
    else:
        arr = [num]
    ordToSeriesMap[ordinal] = arr
    return ordToSeriesMap

def initMap():
    ordToSeriesMap = {}
    maxLimit = (math.sqrt(80001)-1)/2
    for i in range(3,9):
        for n in range(1, math.ceil(maxLimit)):
            f = figurate(i,n)
            if f < 1000:
                continue
            elif f >= 10000:
                break
            else:
                ordToSeriesMap = appendToMap(ordToSeriesMap, i, int(f))
    return ordToSeriesMap
    
def semiMatch(ref, new):
    if ref == None:
        return True
    refStr, newStr = str(ref), str(new)
    return refStr[2:] == newStr[:2]

def findCycle(ref, ordMap, usedKeys=[], usedNums=[]):
    keys = [k for k in list(ordMap.keys()) if k not in usedKeys]
    if len(keys) == 0:
        if semiMatch(usedNums[len(usedNums)-1], usedNums[0]):
            print(usedNums, sum(usedNums))
        return
    for k in keys:
        for value in ordMap[k]:
            if semiMatch(ref, value):
                usedKeysCopy = usedKeys.copy()
                usedKeysCopy.append(k)
                usedNumsCopy = usedNums.copy()
                usedNumsCopy.append(value)
                findCycle(value, ordMap, usedKeysCopy, usedNumsCopy)
               
if __name__ == '__main__':
    findCycle(None, initMap())