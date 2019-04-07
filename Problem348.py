import math, itertools, sys

def palidrome_gen(max_num_digits):
    num_digits = 2
    req_list = [list(range(1, 10))]
    while num_digits <= max_num_digits:
        num_wo_ref = (num_digits+1)//2
        half = num_digits//2
        if len(req_list) < num_wo_ref:
            req_list.extend([list(range(0, 10))])
        for arr in itertools.product(*req_list):
            str_num = ''.join(map(lambda r: str(r), arr))
            str_num = str_num + str_num[:half][::-1]
            yield(str_num)
        num_digits += 1

def is_square(num):
    sq_root_int = round(math.sqrt(num))
    return num == sq_root_int**3

def calculate():
    num_occurrences = 4
    num_numbers = 5

    result_set = set()
    for strnum in palidrome_gen(20):
        num = int(strnum)
        print(num)
        occurrences = 0
        for cube_base in range(0, int(math.floor(num**(1./3.)))):
            residue = num-cube_base*cube_base*cube_base
            if is_square(residue):
                occurrences+= 1
                if occurrences == num_occurrences:
                    result_set.add(num)
                    if len(result_set) == num_numbers:
                        print('---',result_set)
                        print('---',sum(result_set))
                        sys.exit(0)

if __name__ == '__main__':
    calculate()