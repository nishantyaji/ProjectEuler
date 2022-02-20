from sympy import isprime


def sumDigits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum


def iterate(maxLimit):
    listOfRightTruncHarsh = []
    result = 0
    for i in range(1, 10):
        listOfRightTruncHarsh.append(i)
    for i in range(1, 10):
        for j in range(0, 10):
            num = 10 * i + j
            if num % sumDigits(num) == 0:
                listOfRightTruncHarsh.append(num)

    while len(listOfRightTruncHarsh) > 0 and listOfRightTruncHarsh[0] < maxLimit:
        num = listOfRightTruncHarsh.pop(0)
        for i in range(0, 10):
            numExt = num * 10 + i
            sumDigitsExt = sumDigits(numExt)
            if numExt % sumDigitsExt == 0:
                if numExt > listOfRightTruncHarsh[len(listOfRightTruncHarsh) - 1]:
                    listOfRightTruncHarsh.append(numExt)
                if isprime(int(numExt/sumDigitsExt)):
                    for j in [1, 3, 7, 9]:
                        numExt2 = numExt * 10 + j
                        if numExt2 >= maxLimit:
                            continue
                        if isprime(numExt2):
                            result += numExt2
    return result


if __name__ == '__main__':
    print(iterate(1e14))
