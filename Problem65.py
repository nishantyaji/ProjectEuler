fractions = [2]

for i in range(1,100,1):
    if((i+1)%3 == 0):
        fractions.append((int)(2*(i+1)/3))
    else:
        fractions.append(1)

def calculate(index):
    return recur(index-1, (fractions[index],1))

def recur(index, tuple):
    if(index == 0):
        return(2*tuple[0] + tuple[1], tuple[0])
    else:
        return recur(index-1, (fractions[index]*tuple[0] + tuple[1], tuple[0]))

def sumofdigits(number):
    string = str(number)
    sum = 0
    for x in string:
        sum += int(x)
    return sum

print(sumofdigits(calculate(99)[0]))
