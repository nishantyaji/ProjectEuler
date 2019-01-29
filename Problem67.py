import requests
import numpy

def readTo2DArray():
    url = 'https://projecteuler.net/project/resources/p067_triangle.txt'
    response = requests.get(url)
    data = response.text
    lines = data.split('\n')
    lines = lines[:len(lines)-1] #Last line is empty
    array2d = numpy.zeros((100,100))

    index = 0
    for line in lines:
        indexWithinLine = 0  
        numbers = line.split(' ')
        for number in numbers:
            array2d[index][indexWithinLine] = int(number)
            indexWithinLine = indexWithinLine+1
        index = index+1
    return array2d

def calculateMax(array2d):
    numLines = len(array2d)
    for i in range(1, numLines):
        for j in range(0, i+1, 1):
            if j ==0:
                leftParent = 0
            else:
                leftParent = array2d[i-1][j-1]
            if j == i:
                rightParent = 0
            else:
                rightParent = array2d[i-1][j]
            array2d[i][j] = max([leftParent+array2d[i][j], rightParent+array2d[i][j]])
    maxSum = max(array2d[numLines-1])
    print(maxSum)

def calculate():
    calculateMax(readTo2DArray())

if __name__ == '__main__':
    calculate()