#encoding: utf-8
from collections import defaultdict
import math

L = 6
demand = defaultdict(int)

def solve_one_pipe():
    max_n = []
    all_len = demand.keys()
    for l in all_len:
        max_n.append(int(L / l))
    print(max_n)

def print_demand():
    for k, v in demand.items():
        print(str(k) + '\t' + str(v))

def count_pipe():
    sum = 0
    for _, v in demand.items():
        sum += v

    return sum

def total_len():
    sum = 0
    for k, v in demand.items():
        sum += k * v
    
    return sum

def read_input(file_name = 'input-2.txt'):
    lines = open(file_name).read().splitlines()
    for line in lines:
        if line.startswith('#'): 
            continue
        try:
            l, n = line.split()
            demand[float(l)] += int(n)
        except:
            pass
        
def main():
    read_input()
    print_demand()
    
    l = total_len()
    print('# of different lengths: %d' % len(demand))
    print('# of sections of steel pipes: %d' % count_pipe())
    print('total length: %.3f' % l)
    min_n = int(math.ceil(l / L))
    print('lower bound for N (most likely unreachable): %d' % min_n)
    
    # solve_one_pipe()


if __name__ == '__main__':
    main()

