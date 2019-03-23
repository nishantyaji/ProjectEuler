import sympy, math, functools, operator, pprint

result_dict = {}

def is_square(n):
    sqr = int(math.sqrt(n))
    n == sqr * sqr

def add_count(n, ways):
    # Will not use n
    if ways in result_dict:
        result_dict[ways] = result_dict[ways]+1
    else:
        result_dict[ways]=1

def add_count_debug(n, ways):
    if ways in result_dict:
        result_dict[ways].append(n)
    else:
        result_dict[ways] = [n]

def calculate(max_limit):
    for n in range(2, (max_limit//4)+1):
        tot = sympy.factorint(n)

        tau = 1
        for base, power in tot.items():
            tau *= (power+1)

        if is_square(n):
            ways = (tau+1)//2
        else:
            ways = tau//2

        add_count(n, ways)
    ans = 0
    for i in range(1, 11):
        ans += result_dict[i]
    print(ans)
        
if __name__ == '__main__':
    max_limit = 1000000
    calculate(max_limit)
    #pprint.pprint(result_dict)