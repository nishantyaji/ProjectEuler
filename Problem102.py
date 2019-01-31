import requests
import numpy

def readTo2DArray():
    url = 'https://projecteuler.net/project/resources/p102_triangles.txt'
    response = requests.get(url)
    data = response.text

    lines = data.split('\n')
    lines = lines[:len(lines)-1] #Last line is empty
    array2d = numpy.zeros((len(lines),6))

    index = 0
    for line in lines:
        indexWithinLine = 0  
        numbers = line.split(',')
        for numberStr in numbers:
            number = int(numberStr)
            array2d[index][indexWithinLine] = int(number)
            indexWithinLine = indexWithinLine+1
        index = index+1
    return array2d

def areaOfTriangle(triangleCoordinates):
    x1, y1, x2, y2, x3, y3 = triangleCoordinates
    area = 0.5 * ( x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    return area

def isOriginInterior(triangleCoordinates):
    x1, y1, x2, y2, x3, y3 = triangleCoordinates
    areaAll = areaOfTriangle((x1, y1, x2, y2, x3, y3))
    area1 = areaOfTriangle((0, 0, x2, y2, x3, y3))     
    area2 = areaOfTriangle((x1, y1, 0, 0, x3, y3))
    area3 = areaOfTriangle((x1, y1, x2, y2, 0, 0))
    return abs(areaAll) == (abs(area1)+abs(area2)+abs(area3))

def calculate():
    array2d = readTo2DArray()
    count = 0
    for line in array2d:
        (x1, y1, x2, y2, x3, y3) = line
        if isOriginInterior((x1, y1, x2, y2, x3, y3)):
            count = count+1
    return count

if __name__ == '__main__':
    print(calculate())